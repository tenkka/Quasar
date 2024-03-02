import pandas as pd

# Input and output file paths
input_file_path = 'milliquas.txt'
output_file_path = 'milliquas.csv'

# Define byte positions based on the provided format
column_positions = [(0, 11), (12, 23), (25, 50), (51, 55), (56, 61), (62, 67), (68, 71),
                    (72, 73), (74, 75), (76, 82), (83, 89), (90, 96), (97, 119), (120, 142), (143, 165), (166, 188)]

# Column names
columns = ['RA', 'DEC', 'Name', 'Type', 'Rmag', 'Bmag', 'Comment', 'R', 'B', 'Z', 'Cite', 'Zcite', 'Xname', 'Rname', 'Lobe1', 'Lobe2']

if __name__ == "__main__":
    print('start read')
    # Read the fixed-width-format file into a DataFrame
    df = pd.read_fwf(input_file_path, colspecs=column_positions, header=None, names=columns)

    # Write the DataFrame to a CSV file
    df.to_csv(output_file_path, index=False)

    print(f"Conversion completed. CSV file saved to {output_file_path}")