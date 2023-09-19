# Database Initializer CLI

This command-line tool,  **Database Initializer CLI** , allows you to create and initialize a SQLite database with tables defined in a schema file. It follows object-oriented programming (OOP) principles and some clean code practices for better code organization and readability.


## Features

* **Database Connection** : Establishes a connection to the SQLite database.
* **Database Cursor** : Creates a cursor for executing SQL queries.
* **Schema File Parsing** : Reads and parses the schema file to extract SQL statements.
* **Table Creation** : Creates tables in the database based on the parsed schema.
* **Commit Changes** : Commits the changes to the database.
* **Connection Closure** : Closes the database connection when done.

## Prerequisites

* Python 3.x installed
* Schema file (e.g., `schema.sql`) containing CREATE TABLE statements

## Usage

To use the Database Initialization CLI, follow these steps:

1. Clone this repository to your local machine:
   `git clone https://github.com/micael-ortega/database-initializer.git `

2. Navigate to the project directory:
   `cd database-initializer`

3. Run the setup shell script:
   `./setup`

4. Run the CLI tool:
   `dbinit <database_name> <schema_file>`


## Example

`dbinit mydb.db example/schema.sql`

---
