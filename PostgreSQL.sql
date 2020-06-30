-- PostgreSQL, also known as Postgres,
-- An extremely powerful database engine. At a high level, PostgreSQL consists of two pieces, a server and clients. The server is a program that manages databases and handles queries. Clients communicate back and forth to the server. Only the server ever directly accesses the databases -- the clients can only make requests to the server.
-- PostgreSQL uses port 5432, clients would be able to connect using this port
--
-- PostgreSQL has many clients, one is Graphical Clients. Python client is called Psycopg2, simialar to sqlite3 library
_______________________________________________________________________________


PostgreSQL in Python:
import psycopg2 -- defaults to connecting to 5432 server on local machine
db = psycopg2.connect('dbname=postgres user=postgres') -- specify unique database and user, can have multiple ones
cursor = db.cursor()

-- Execute a query
query = 'SELECT * FROM table;'
cursor.execute(query)

-- Transactions: collections of user changes in a block which are executed at the same time to prevent repeating failures
-- A new transaction will open with every new Connection to psycopg2
-- All transactions are pending until commited or rolledback

-- Commit a transaction: All queries that run until the commit method will be placed into the same transaction block
db.commit() -- connection method, commit all pending transactions

-- Reverse a transaction: if we don't want to apply the changes
db.rollback() -- connection method, reverse all transactions in the block

-- Close a connection
db.close()

-- Autocommit a change
db.autocommit = True -- After connecting to db

-- Fetch and print rows
result = cursor.fetchall()
-- OR
result = cursor.fetchone() -- Use print() to print results
________________________________________________________________________________


PostgreSQL Shell:
-- PSQL Command Line Tool
-- Automatically connects to port 5432, dbname and user default to 'postgresql'
-- Start PostgreSQL
$ psql
-- OUT
db=#

-- Running a general query will autocommit
-- PostgreSQL special commands start with a backslash (\)

-- List all databases
db=# \l

-- List all tables in the current database
db=# \dt

-- List all users
db=# \du

-- See all privileges of a user
db=# \dp

-- See all special functions
db=# \?

-- Exit PSQL
db=# \q

-- Connect to a different database
psql -d dbName -- Will start connectd to the specified database

-- Connect to psql as userName
psql -u userName

-- Create a new user
db=# CREATE ROLE userName;

-- Allow Login access
db=# CREATE ROLE userName WITH LOGIN;

-- Create a password
db=# CREATE ROLE userName WITH LOGIN PASSWORD 'password';

-- Allow user to create databases
db=# CREATE ROLE userName WITH CREATEDB LOGIN PASSWORD 'password';

-- Allows user to create other users
db=# CREATE ROLE userName WITH CREATEROLE LOGIN PASSWORD 'password';

-- Makes the user a superuser
db=# CREATE ROLE userName WITH LOGIN PASSWORD 'password' SUPERUSER;

-- Give users permissions to C.R.U.D tables in the database
GRANT STATEMENT ON table TO userName; -- STATEMENT could be SELECT, INSERT, UPDATE, DELETE, etc.

-- GIve user multiple permissions at once
GRANT SELECT, INSERT, UPDATE, DELETE ON table TO userName;

-- Shorcut ^^
GRANT ALL PRIVILEGES ON table TO userName;

-- Remove permissions from a user
REVOKE ALL PRIVILEGES ON table FROM userName; -- Same as GRANT options
