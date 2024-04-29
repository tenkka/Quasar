import subprocess
import tempfile
import os

def merge_two_catalogues(catalogue_one_file, catalogue_two_file, out_catalogue_file, stilts_jar_with_path="stilts.jar", radius=3, create_out=False):
    tmp_catfile_name = tempfile.NamedTemporaryFile().name
    subprocess.run(["java", "-jar", "-Xmx96G", stilts_jar_with_path, "tskymatch2",
                    "in1=" + catalogue_one_file, "in2=" + catalogue_two_file,
                    "ifmt1=csv", "ifmt2=csv", "out=" + tmp_catfile_name, "ofmt=csv",
                    "ra1=RA", "dec1=DEC", "ra2=RA", "dec2=DEC", "error=" + str(radius),
                    "join=2not1"], check=True)
    if create_out:
        with open(out_catalogue_file, "w") as outfile:
            with open(catalogue_one_file, "r") as infile:
                outfile.write(infile.read())
    with open(tmp_catfile_name, "r") as tmpfile:
        with open(out_catalogue_file, "a") as outfile:
            next(tmpfile)  # Skip header
            outfile.write(tmpfile.read())
    os.remove(tmp_catfile_name)

def merge_multiple_catalogues(catalogues, out_file):
    if len(catalogues) == 1:
        with open(catalogues[0]) as infile:
            with open(out_file, 'w') as outfile:
                outfile.write(infile.read())
    else:
        merge = catalogues[0]
        create = True
        for i in range(1, len(catalogues)):
            c2 = catalogues[i]
            print('merging',merge,c2)
            merge_two_catalogues(merge, c2, out_file, create_out=create)
            print('merge complete')
            merge = out_file
            create = False


# merge_multiple_catalogues(['data/quaia23RADECName.csv', 'data/r90cat_radecid.csv', 'data/milliquas.csv', 'GDR2uW_RADECName.csv'], 'data/new_merge.csv')
# merge_two_catalogues('data/merge.csv', 'data/r90cat_radecid.csv', 'data/merge.csv', create_out=True)