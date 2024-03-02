import pandas as pd
import sqlite3

csv_file_path = 'milliquas.csv'
sqlite_db_path = 'quasar.db'

# Read CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Connect to SQLite database
conn = sqlite3.connect(sqlite_db_path)

# Save DataFrame to SQLite database
df.to_sql('milliquas', conn, index=False, if_exists='replace')

# Close the database connection
conn.close()

print(f"CSV data saved to SQLite database: {sqlite_db_path}")