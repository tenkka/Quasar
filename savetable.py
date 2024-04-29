import pandas as pd
import sqlite3
import os

class TableSaver:
    def __init__(self, db_path, summary_file='summary.txt'):
        self.db_path = db_path
        self.summary_file = summary_file

    def write_csv_to_db(self, csv_path, name):
        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_path)

        # Connect to SQLite database
        conn = sqlite3.connect(self.db_path)

        # Save DataFrame to SQLite database
        df.to_sql(name, conn, index=False, if_exists='replace')

        # Get information for the summary line
        table_name = name
        column_names = list(df.columns)
        row_count = len(df)
        file_size = os.path.getsize(csv_path)  # in bytes

        # Write the summary line to the summary file
        with open(self.summary_file, 'a') as summary_file:
            summary_line = f"{table_name}, {column_names}, {row_count}, {file_size} bytes\n"
            summary_file.write(summary_line)

        # Close the database connection
        conn.close()

        print(f"CSV data saved to SQLite database: {self.db_path}")
        print(f"Summary line written to {self.summary_file}")

    def write_binary_to_db(self, df, name, file_size):
        conn = sqlite3.connect(self.db_path)

        # Save DataFrame to SQLite database
        df.to_sql(name, conn, index=False, if_exists='replace')

        # Get information for the summary line
        table_name = name
        column_names = list(df.columns)
        row_count = len(df)

        # Write the summary line to the summary file
        with open(self.summary_file, 'a') as summary_file:
            summary_line = f"{table_name}, {column_names}, {row_count}, {file_size} bytes\n"
            summary_file.write(summary_line)

        # Close the database connection
        conn.close()

        print(f"CSV data saved to SQLite database: {self.db_path}")
        print(f"Summary line written to {self.summary_file}")