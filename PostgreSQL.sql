# PostgreSQL, also known as Postgres,
# An extremely powerful database engine. At a high level, PostgreSQL consists of two pieces, a server and clients. The server is a program that manages databases and handles queries. Clients communicate back and forth to the server. Only the server ever directly accesses the databases -- the clients can only make requests to the server.
# PostgreSQL uses port 5432, clients would be able to connect using this port

# PostgreSQL has many clients, one is Graphical Clients. Python client is called Psycopg2, simialar to sqlite3 library
import psycopg2 # defaults to connecting to 5432 server on local machine
db = psycopg2.connect('dbname=postgres user=postgres') # specify unique database and user, can have multiple ones
cursor = db.cursor()

# Close a connection
db.close()

# Execute a query
query = 'SELECT * FROM table;'
cursor.execute(query)

# Transactions: collections of user changes in a block which are executed at the same time to prevent repeating failures
# A new transaction will open with every new Connection to psycopg2
# All transactions are pending until commited or rolledback

# Commit a transaction: All queries that run until the commit method will be placed into the same transaction block
db.commit() # connection method, commit all pending transactions

# Reverse a transaction: if we don't want to apply the changes
db.rollback() # connection method, reverse all transactions in the block 
