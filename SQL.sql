SQL (Structured Query Language):
-- Communicates with a DBMS (Database Management System) to query datasets.

-- C.R.U.D Operations
-- Create
-- Read
-- Update
-- Delete

-- Schema diagram: How tables in databse are linked with which columns
_______________________________________________________________________________


CLAUSES:
-- Query order
1. SELECT *
2.   FROM some_table
3.  WHERE some_condition
4.  GROUP BY col
5. HAVING some_condition
6. ORDER BY some_column
7. LIMIT some_limit;

-- The order in which the clauses run:
1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

-- Get data, cols, table, etc.
SELECT Clause

-- Which table to get te data from
FROM Clause

-- Used to filter our data
WHERE Clause

-- Comparison Operators
Less Than <
Less or equal to <=
Greater than >
Greater or equal to >=
Equal to = or IS
Not equal to != or <> or IS NOT
Find in IN

-- Used to filter data based on TWO criteria
AND Clause

-- Filter data based on either of TWO criteria
OR Clause

-- Specify the order
ORDER BY Clause

-- Rename results table columns
AS Clause

-- Select unique Values of a column
SELECT DISTINCT Clause

-- If/Then Logic
CASE Clause

-- Group Summary Stats
GROUP BY Clause

-- Filter out GROUP BY Clause
HAVING Clause

-- Subquery
WITH Clause

-- Permenant subquery
CREATE VIEW Clause

-- Concatenate strings
|| Operator

-- Match names similar to pattern
LIKE Operator

-- Categorize if/then options for a new column
CASE Statement
________________________________________________________________________________


CREATE:
-- Create a database
CREATE DATABASE dbName;

-- Create a database and specify owner
CREATE DATABASE dbName OWNER user;

-- Create a database table
CREATE TABLE table (
  col1 co1_type,
  col2 col2_type,
  col3 col3_type,
  ...
);

-- Data Types
-- TEXT, CHARACTER, VARCAHR, NCHAR, NVARCHAR, DATETIME: For strings
-- INTEGER, INT, SMALLINT, BIGINT, INT8: Numeric
-- REAL, DOUBLE, FLOAT: Weights, Averages
-- NUMERIC, DECIMAL, BOOLEAN: DeCIMALS
-- BLOB: Binary data

-- Primary Key: Unique id for each row, can't have to with the same
CREATE TABLE table (
  col1 co1_type PRIMARY KEY,
  col2 col2_type,
  col3 col3_type
);

-- Foreign Key: A column in one table that is a primary key in another table.
CREATE TABLE table (
  col1 co1_type PRIMARY KEY,
  col2 col2_type,
  col3 col3_type,
  FOREIGN KEY (col2) REFERENCES table(col)
);

-- Composite or Compound Key
CREATE TABLE table (
  col1 co1_type,
  col2 col2_type,
  col3 col3_type,
  PRIMARY KEY (col1, col2) -- Same thing with FOREIGN KEYS
);

-- Add rows
INSERT INTO table (
  col1,
  col2,
  col3,
) VALUES (
  val1,
  val2,
  val3
);

-- Add val to all columns of the row
INSERT INTO table VALUES (val1, val2, val3);

-- Add val to all columns seprated by rows
INSERT INTO table
VALUES
  (val1, val2, val3),
  (val4, val5, val6),
  ...;
________________________________________________________________________________


READ:
-- Structured code to CRUD databases
-- Ask DBMS software to run the code and display the results

-- Check schema overview
SELECT
    name,
    type
FROM sqlite_master
WHERE type IN ("table","view");

-- Return Schema of a table
PRAGMA table_info(table);

-- Select ALL columns from table
SELECT *
  FROM table; -- Always end command with (;)

-- Select top n columns from table
SELECT *
  FROM table
 LIMIT n; -- Eq. to df.head()

-- Select a column from table
SELECT table.column
  FROM table; -- Eq. to df[col]

-- Select mulitple columns from table
SELECT table.col1, table.col2
  FROM table; -- Eq. to df.loc[col1, col2]

-- Filter rows by specific criteria
SELECT *
  FROM table -- Eq. to df.loc[col1 == bool]
 WHERE condition; -- Use the comparison operators

-- Filter rows by TWO criterias
SELECT *
  FROM table
 WHERE condition1
   AND condition2; -- Eq. to df.loc[col1 == bool & col2 == bool]

-- Filter rows by either of TWO criteria
SELECT *
  FROM table
 WHERE condition1
   OR condition2; -- Eq. to df.loc[col1 == bool | col2 == bool]

-- Order rows by a column
SELECT *
  FROM table
 WHERE condition -- Eq. to df.sorted
 ORDER BY col; -- Defaults to AESC order

-- Order rows by a column in DESCENDING order
SELECT *
  FROM table
 WHERE condition
 ORDER BY col DESC;

-- Order rows by a column using numerical id
SELECT table.column1, table.column2 -- numbered 1 2 in order, like aliases
  FROM table
 WHERE condition -- Can be used with GROUP BY also
 ORDER BY 2 DESC; -- 2 means the second column from the SELECT clause

-- Select and Rename column, KNOWN as an Alias
SELECT table.column AS 'new_col'
  FROM table;
-- OR
SELECT table.column 'new_col'
  FROM table;

-- Select and rename table
SELECT *
  FROM table AS t; -- Also optional to not include ^^

-- Reference renamed cols in queries
SELECT table.column1 'c1', table.column2 'c2'
  FROM table
 WHERE c1 = condition1 -- Use the rename from SELECT
   AND c2 = condition2
 ORDER BY c2 DESC

-- Select Unique values of a column
SELECT DISTINCT table.column
  FROM table;

-- Select based on if/then logic
SELECT table.column,
       CASE -- Indicates cases
       WHEN <bool_1> THEN <value_1> -- Eq. to if/elif
       WHEN <bool_2> THEN <value_2>
       ELSE <value_3> -- Fallback value
       END AS <new_column_name> -- Indicates where Case ends
  FROM table;

-- Find values in rows
SELECT table.column
  FROM table
 WHERE condition IN table.column;

-- Find NULL values in rows
SELECT table.column
  FROM table
 WHERE table.colum IS NULL;

-- Find Not NULL values in rows
SELECT table.column
  FROM table
 WHERE table.column IS NOT NULL;

-- Concatenate columns: Concatenate operator ||
SELECT 'string' || table.col
  FROM table; -- Output 'stringcol

-- Match similar to pattern
SELECT table.col
  FROM table
 WHERE table.col LIKE '[pattern]' -- Case insensitive
-- %pattern will match at end of string
-- pattern% will match at start of string
-- %pattern% will match anywhere within string

-- If/then new column
SELECT
    table.col,
    CASE
        WHEN condition1 THEN val1 -- Can use LIKE oeprator as condition
        WHEN condition2 THEN val2 -- Eq. to If/Elif/Else
        ELSE val3
        END
        AS new_col
  FROM table;
________________________________________________________________________________


UPDATE:
-- Change values for existing rows
UPDATE table
SET col = exp;

-- Upadte a single value of a row
UPDATE table
SET col = exp
WHERE row_id = INT;

-- Update using subqueries
UPDATE table
SET col = [subquery]

-- Update a column with a column or aggfunc
UPDATE table
SET col2 = col1 * INT;

-- Update more than one column at once
UPDATE table
SET
  col1 = exp,
  col2 = exp;

-- Add a column to an existing table
ALTER TABLE table
ADD COLUMN col col_type;
________________________________________________________________________________


DELETE:
-- Delete
DROP TABLE table;

-- Delete a VIEW
DROP VIEW database.table;

-- Delete a Database
DROP DATABASE dbName;
________________________________________________________________________________


OPERATIONS:
-- Select the minimum value of a column
SELECT MIN(table.column) -- See also: MAX, AVG, SUM
  FROM table;

-- Count the rows of a column
SELECT COUNT(table.column) -- Use COUNT(*), COUNT(col) to find NULL
  FROM table;

-- Count the number of Unique values of a column
SELECT COUNT(DISTINCT table.column)
  FROM table;

-- Count the number of characters in a column entry
SELECT LENGTH(table.column)
  FROM table; -- Eq. to Len(str)

-- Replace a string with lower case
SELECT LOWER(table.column)
  FROM table; -- Eq. to df.lower()

-- Round decimals
SELECT ROUND(table.column, n) -- n is number of decimal places
  FROM table;

-- Convert Dtype
SELECT CAST(table.column1 AS Float), CAST(table.column2 AS Int) AS new_name
  FROM table; -- Eq. to df.str.astype

-- Concatenate strings
SELECT str || str
  FROM table; -- Eq. to str + str

-- Group By Statistics
SELECT AGGFUNC(table.column) AS <new_name>
  FROM table
GROUP BY table.column1; -- Eq. to pivot table

-- Group by multiple columns
SELECT AGGFUNC(table.column) AS <new_name>
  FROM table
GROUP BY table.column1, table.column2;

-- Group by with conditions
SELECT AGGFUNC(table.column) AS <new_name>
  FROM table
GROUP BY table.column1
HAVING condition; -- Eq. to WHERE but for GROUP BY
________________________________________________________________________________


SUBQUERIES:
-- General Format
SELECT table.column
  FROM table
 WHERE some_condition > (subquery); -- Eq. to Nested Functions

-- SELECT Subquery
SELECT table.column
  FROM table
 WHERE some_condition > (SELECT AGGFUNC(table.column)
                            FROM table
                          );
-- Returning Multiple Results in Subqueries
SELECT table.column
  FROM table
 WHERE condition IN (SELECT table.column
                      FROM table
                    GROUP BY condition
                  ORDER BY AGGFUNC(col)
                );

-- Create a subquery at the beginning of the SELECT
WITH alias AS (SELECT table.column
                     FROM table
                   GROUP BY condition
                 ORDER BY AGGFUNC(col)
               )
SELECT table.column
  FROM table
 WHERE condition IN alias;

-- Create multiple subqueries at the beginning
WITH
    [alias_name] AS ([subquery]),
    [alias_name_2] AS ([subquery_2]),
    [alias_name_3] AS ([subquery_3])

SELECT [main_query] -- Can use the result of the first subquery in subsequent subqueries

-- Defaults to temporary, to create a permanent subquery
CREATE VIEW database.view_name AS
  SELECT * FROM database.table;
________________________________________________________________________________


JOINS AND UNIONS:
-- Inner Join
SElECT * FROM table1 -- include only rows from each table that match ON
INNER JOIN table2 ON table1.column = table2.column; -- Think intersection of Venn Diagram

-- Left Join
SELECT * FROM table1 -- Include all rows from inner plus any rows from table1
LEFT JOIN table2 ON table1.column = table2.column; -- Think Intersection + table1 of Venn

-- Right Join
SELECT * FROM table2 -- Include all rows from inne plus anty rows from table2
RIGHT JOIN table1 ON table1.column = table2.column; -- Think Int. + Right of Venn Diagram

-- FULL OUTER Join
SELECT * FROM table1
FULL OUTER JOIN table2 ON table1.column = table2.column; -- Like UNION of VennDiagram

-- Joining three tables
SELECT table1.col FROM table1
JOIN table2 ON table1.col = table2.col
JOIN table3 ON table2.col = table3.col; -- Executes in order of listed joins

-- Recursive joins: joining a table to itself
SELECT t1.col, t2.col FROM table1 t1 -- Use inner or left join like normal
INNER JOIN table2 t2 ON t1.col = t2.col; -- Use different aliases for tables

-- Union: Everything inside Venn Diagram
SELECT table1.col -- Must contain the same number of columns
  FROM table1 -- Eq. to OR in pyhton
UNION
SELECT table2.col
  FROM table2;

-- Intersect: The middle intersection of Venn Diagram
SELECT table1.col -- Eq. to AND in python
  FROM table1
INTERSECT
SELECT table2.col
  FROM table2;

-- Except: The first staement but not the second
SELECT table1.col -- Eq. to AND NOT in python
  FROM table1
EXCEPT
SELECT table2.col
  FROM table2;
________________________________________________________________________________


QUERY PLANS:
-- Get a high level query plan of the SELECT statement
EXPLAIN QUERY PLAN SELECT * FROM table;
-- OUTPUT
[(0, 0, 0, 'SCAN TABLE table')] -- Returned as a tuple, means every row in table had to accessed to evalute query
