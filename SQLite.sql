SQLITE SHELL:
-- Run SQLite in Jupyter Notebook
%%capture
%load_ext sql
%sql sqlite:///file.db -- Use %%sql before every query

-- Que up sqlite shell
$ sqlite3 database.db
sqlite>

-- Create new database
$sqlite3 new_database.db

-- SQLite special commands start with a (.)
-- Show header column
sqlite> .headers on -- Known as Dot Commands like Options

-- Show column mode
sqlite> .mode column

-- Documentation
sqlite> .help

-- display a list of all tables and views in the current database
sqlite> .tables

-- Run Ubuntu commands in sqlite
sqlite> .shell [command]

-- Check created table schema
sqlite> .schema table

-- Exit sqlite shell
sqlite> .quit

________________________________________________________________________________


SQLITE IN PYTHON:
-- import
import sqlite3

-- Connect database
db = sqlite3.connect('database.db') -- function, creates a connection instance that blocks anyone but you

-- Return a Cursor instance
cursor = db.cursor() -- Connection instance method, then write SQL code in STRINGS

-- Run an SQLite query
query = 'select * from table'
cursor.execute(query) -- Cursor method
results = cursor.fetchall() -- store result as a vairable
print(results[0:3])

-- Run query shortcut (SKips creating a cursor oject)
query = 'select * from table'
result = db.execute(query).fetchall() -- method chaining

-- Return a single result
result = cursor.fetchone() -- Cursor method
result2 = cursor.fetchone() -- has an interal counter, auto increment by 1

-- Return n results
results = cursor.fetchmany(n) -- cursor method, n=int

-- Close database connection
db.close() -- Connection method, v imp to close bc connection is secure as above ^^
