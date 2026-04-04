import pandas as pd
import sqlite3
import os

def create_and_write_sqlite(csv_filepath, db_name, table_name):
    """
    Creates a SQLite database (if it doesn't exist), 
    defines a table based on CSV headers, and writes the data.
    """
    # 1. Check if the CSV exists to avoid errors
    if not os.path.exists(csv_filepath):
        print(f"Error: File '{csv_filepath}' not found.")
        return

    # 2. Connect to SQLite (creates the file automatically)
    conn = sqlite3.connect(db_name)
    
    try:
        # 3. Read CSV and Write to SQL
        # 'chunksize' is useful if your CSV is larger than your RAM
        # 'if_exists=replace' creates the table if it's new, or overwrites if old
        print(f"Reading {csv_filepath}...")
        df = pd.read_csv(csv_filepath)
        
        print(f"Writing to {db_name} in table '{table_name}'...")
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        # 4. Verify by counting rows
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        print(f"✅ Success! Table '{table_name}' created with {row_count} rows.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
    
    finally:
        # Always close the connection
        conn.close()

# --- Execution ---
# Replace these with your actual filenames
CSV_FILE = "employee_data.csv" 
DATABASE = "Corporate.sqlite"
TABLE = "employee_data"

create_and_write_sqlite(CSV_FILE, DATABASE, TABLE)