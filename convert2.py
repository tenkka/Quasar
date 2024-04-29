import csv

# Input and output file paths
txt_file_path = 'data/quaia23RADECName.txt'
csv_file_path = 'data/quaia23RADECName.csv'

# Read the lines from the text file
with open(txt_file_path, 'r') as txt_file:
    lines = txt_file.readlines()

# Extracting headers and data from the lines
headers = lines[0].strip().split(',')
data_lines = [line.strip().split(',') for line in lines[1:]]

# Write to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the headers
    csv_writer.writerow(headers)

    # Write the data
    csv_writer.writerows(data_lines)

print(f"Conversion completed. CSV file saved at: {csv_file_path}")