SQL (Structured Query Language):
-- Communicates with a DBMS to query datasets.
-- C.R.U.D Operations

-- Create
-- Read
-- Update
-- Delete
________________________________________________________________________________


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
________________________________________________________________________________


READ:
-- Structured code to CRUD databases
-- Ask DBMS software to run the code and display the results

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

-- Select and Rename column, KNOWN as an Alias
SELECT table.column AS 'new_col'
  FROM table;
-- OR
SELECT table.column 'new_col'
  FROM table;

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

________________________________________________________________________________
