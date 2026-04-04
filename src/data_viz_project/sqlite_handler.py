import sqlite3
import pandas as pd
import os

class EmployeeDB:
    def __init__(self, db_name="Corporate.sqlite"):
        self.db_name = db_name
        self.table_name = "employee_data"
        # self._create_table_if_not_exists()

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def _create_table_if_not_exists(self):
        """Initializes the table with a standard schema if it doesn't exist."""
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT,
            salary REAL,
            joining_date TEXT
        )
        """
        with self._get_connection() as conn:
            conn.execute(query)

    # --- CRUD OPERATIONS ---

    def create_employee(self, name, role, salary, joining_date):
        """INSERT: Add a new employee."""
        query = f"INSERT INTO {self.table_name} (name, role, salary, joining_date) VALUES (?, ?, ?, ?)"
        with self._get_connection() as conn:
            conn.execute(query, (name, role, salary, joining_date))
        print(f"✅ Employee '{name}' added successfully.")

    def read_all(self):
        """READ: Get all records as a Pandas DataFrame (best for your UI)."""
        with self._get_connection() as conn:
            return pd.read_sql(f"SELECT * FROM {self.table_name}", conn)

    def read_custom(self,query):
        """READ: Get all records as a Pandas DataFrame (best for your UI)."""
        with self._get_connection() as conn:
            return pd.read_sql(f"{query}", conn)

    def update_salary(self, emp_id, new_salary):
        """UPDATE: Change salary for a specific ID."""
        query = f"UPDATE {self.table_name} SET salary = ? WHERE id = ?"
        with self._get_connection() as conn:
            conn.execute(query, (new_salary, emp_id))
        print(f"✅ Salary updated for ID {emp_id}.")

    def delete_employee(self, emp_id):
        """DELETE: Remove an employee by ID."""
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        with self._get_connection() as conn:
            conn.execute(query, (emp_id,))
        print(f"✅ Employee ID {emp_id} deleted.")

    # --- SCHEMA RETRIEVAL ---

    def get_schema(self):
        """Returns the column names and data types of the table."""
        with self._get_connection() as conn:
            # PRAGMA table_info is the standard SQLite way to get metadata
            schema_info = pd.read_sql(f"PRAGMA table_info({self.table_name})", conn)
            # Returning a cleaned up version showing only Name and Type
            return schema_info[['name', 'type']]

# --- Example Usage ---

# db = EmployeeDB("office.db")

# # 1. Create
# db.create_employee("John Doe", "Developer", 75000, "2024-01-15")
# db.create_employee("Jane Smith", "Designer", 68000, "2024-02-10")

# # 2. Read (Schema)
# print("\n--- Table Schema ---")
# print(db.get_schema())

# # 3. Read (Data)
# print("\n--- Current Employees ---")
# print(db.read_all())

# # 4. Update
# db.update_salary(1, 80000)

# # 5. Delete
# # db.delete_employee(2)