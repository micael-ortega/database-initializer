import sqlite3 as sq
import re
import time
import sys


class DatabaseInitializer:
    SLEEP = time.sleep(0.08)
    def __init__(self):
        self.db_name = None
        self.schema = None
        self.conn = None
        self.cursor = None
        self.table_names = None
        self.stmts = None

    def setup_db(self):
        '''Set the database name and schema based on CLI arguments'''
        self.read_console()

    def create_connection(self):
        '''Connect to the database.'''
        self.setup_db()
        print("\r✅ Assuring database connection...", end=" ", flush=True)
        try:
            self.conn = sq.connect(self.db_name)
            self.SLEEP
            print(f"\r✅ - Assuring database connection... Done!", flush=True)
        except sq.Error as e:
            print("Error connecting to database:", e)

    def create_cursor(self):
        '''Create database cursor.'''
        print("🖱️  - Assuring database cursor...", end=" ", flush=True)
        try:
            self.cursor = self.conn.cursor()
            self.SLEEP
            print(f"\r🖱️  - Assuring database cursor... Done!", flush=True)
        except sq.Error as e:
            print("Error creating cursor:", e)

    def read_schema_from_file(self):
        '''Read schemas presented on selected SQL file'''
        print("⏳ - Reading schema...", end=" ", flush=True)
        try:
            with open(self.schema, "r") as f:
                lines = "\n".join(f.readlines())
                lines = lines.replace("\n", " ")
                stmts = lines.split(";")
                stmts = [stmt.strip() for stmt in stmts if stmt.strip()]
                self.SLEEP
                print("\r⏳ - Reading schema... Done!", flush=True)
                self.stmts = stmts
        except RuntimeError as e:
            print("Error reading schema file:", e)

    def read_table_names(self):
        '''Extracts table names from SQL statments'''
        self.read_schema_from_file()
        self.table_names = []
        for stmt in self.stmts:
            pattern = r'CREATE TABLE(?: IF NOT EXISTS)? (\w+)'
            found_table_name = re.findall(pattern, stmt)
            self.table_names.extend(found_table_name)

    def create_table(self):
        '''Create database tables based on SQL statments'''
        self.read_table_names()
        for i, table_name in enumerate(self.table_names):
            if table_name:
                print(
                    f"\r📦 - Creating table: {self.table_names[i]}...",
                    end=" ",
                    flush=True
                )
                try:
                    self.cursor.execute(self.stmts[i])
                    self.SLEEP
                    print(
                        f"\r📦 - Creating table: {self.table_names[i]}... Done!",
                        flush=True
                    )
                except sq.Error as e:
                    print("Error creating table:", e)

    def commit_session(self):
        '''Commit changes to the database'''
        print("\r📝 - Commiting changes to database...", end=" ", flush=True)
        try:
            self.conn.commit()
            self.SLEEP
            print("\r📝 - Commiting changes to database...Done!", flush=True)
        except sq.Error as e:
            print("Error commiting changes to database:", e)

    def close_connection(self):
        '''Closes database connection'''
        print("\r🔌 - Closing connection to database...", end=" ", flush=True)
        try:
            self.conn.close()
            print("\r🔌 - Closing connection to database...Done!", flush=True)
        except sq.Error as e:
            print("Error closing connection to database")


    def read_console(self):
        '''Reads console args'''
        if len(sys.argv) < 3:
            print("Usage: db_init <database_name> <schema>")
            sys.exit(1)
        db_name = sys.argv[1]
        schema_file = sys.argv[2]
        self.db_name = db_name
        self.schema = schema_file
