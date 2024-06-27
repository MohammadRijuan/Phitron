/* -- Write the difference between Primary Key and Composite Primary Key

1. A primary key is a unique identifier for a single row within a database table
2. A composite primary key consists of two or more columns that together uniquely identify each row in a table.

diffrences->
1. there can only be one primary key per table
2. Typically consists of a single column, often an auto-incremented integer or a uniquely identifying attribute.
3.  Primary key is a single column, whereas composite primary key is made up of multiple columns.
4. Primary key enforces uniqueness on its own column, while composite primary key enforces uniqueness across the combination of columns.

*/

/* Write the difference between using JOIN Query and not using JOIN query

1. A JOIN syntax in mySQL combines rows from two or more tables along with column between them.
2. Without using JOIN syntax, we might retrieve data separately from each table and manually link them using application code or by running multiple queries.
3. In many ways, database optimize JOIN syntax, resulting in efficient query execution compared to mannual methods.
4. Mannual linking can lead to complex relation and error-prone code, especially when contacting with more than two tables or complex relationships.
Example->
SUPPOSE THERE ARE TWO TABLE ONE IS EMPLOYEES AND 2ND ONE IS DEPARTMENTS 

-- without using join syntax how we can join two table
-- WE CAN WRITE THIS ONE TOO

-- SELECT FIRST_NAME,DEPARTMENT_NAME
SELECT EMPLOYEES.FIRST_NAME , DEPARTMENTS.DEPARTMENT_NAME -- THIS ONE IS FOR BEST PRACTICE TO UNDERSTAND
FROM EMPLOYEES, DEPARTMENTS
WHERE EMPLOYEES.DEPARTMENT_ID=DEPARTMENTS.DEPARTMENT_ID;


-- USING JOIN SYNTAX

SELECT EMPLOYEES.FIRST_NAME,DEPARTMENTS.DEPARTMENT_NAME
FROM EMPLOYEES 
             JOIN DEPARTMENTS ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID;
             
SELECT EMPLOYEES.FIRST_NAME,DEPARTMENTS.DEPARTMENT_NAME
FROM EMPLOYEES 
             INNER JOIN DEPARTMENTS ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID;
             
			*/
            
/* Create a table of Employees which has the following fields
First Name
Last Name
Date of Birth
Department Id
Salary

Create a table of Departments which has the following fields

Department Id
Department Name
Create both of the tables using proper constraints

Answer : */

CREATE DATABASE PRACTICES;
USE PRACTICES;

CREATE TABLE EMPLOYEES(
        FIRST_NAME VARCHAR(50) NOT NULL,
        LAST_NAME VARCHAR(50) NOT NULL,
        DATE_OF_BIRTH DATE ,
        DEPARTMENT_ID INT PRIMARY KEY,
        SALARY DECIMAL(10,2)
        
);

CREATE TABLE DEPARTMENTS(
      DEPARTMENT_NAME VARCHAR(50),
      DEPARTMENT_ID INT NOT NULL
      
);

--  Write SQL Query to get the second max salary

USE DUMMYDB; 

SELECT *
FROM EMPLOYEES
WHERE SALARY =(SELECT MAX(SALARY)
               FROM EMPLOYEES
               WHERE SALARY < (SELECT MAX(SALARY)
                               FROM EMPLOYEES)
			);
            
-- Write SQL Query to show  the department names and the average salary of the departments

SELECT DEPARTMENTS.DEPARTMENT_NAME,AVG(SALARY)
FROM DEPARTMENTS 
               JOIN EMPLOYEES
                   ON DEPARTMENTS.DEPARTMENT_ID = EMPLOYEES.DEPARTMENT_ID
GROUP BY EMPLOYEES.DEPARTMENT_ID;

--  Illustrate the INNER, LEFT, RIGHT, SELF Joins

-- USING LEFT JOIN SHOW DEPARTMENTS WHERE THERE ARE NO EMPLOYEES

SELECT DEPARTMENTS.DEPARTMENT_NAME
FROM DEPARTMENTS
             LEFT JOIN EMPLOYEES
                  ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
WHERE EMPLOYEES.DEPARTMENT_ID IS NULL;

-- USING RIGHT JOIN SHOW DEPARTMENTS WHERE THERE ARE NO EMPLOYEES

SELECT DEPARTMENTS.DEPARTMENT_NAME
FROM EMPLOYEES
             RIGHT JOIN DEPARTMENTS
                  ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
WHERE EMPLOYEES.DEPARTMENT_ID IS NULL;
                  
-- USING INNER JOIN HIDING DEPARTMENTS WHERE THERE ARE NO EMPLOYEES

SELECT DEPARTMENTS.DEPARTMENT_NAME
FROM EMPLOYEES
             INNER JOIN DEPARTMENTS
                  ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
GROUP BY EMPLOYEES.DEPARTMENT_ID;

/* -- What is a subquery? Write with an example

ANSWER : A subquery, is a query nested inside another SQL query (KNOWN AS A NESTED QUERY). 
*/

SELECT *
FROM EMPLOYEES
WHERE SALARY =(SELECT MAX(SALARY)
               FROM EMPLOYEES
               WHERE SALARY < (SELECT MAX(SALARY)
                               FROM EMPLOYEES)
               );
-- Show the names of the employees who get less salary than Steven

SELECT FIRST_NAME,SALARY
FROM EMPLOYEES
WHERE SALARY < (SELECT SALARY
                FROM EMPLOYEES
                WHERE FIRST_NAME = 'STEVEN'
                LIMIT 1);
                
-- Count the number of employees of each job type

SELECT JOB_ID,COUNT(*)
FROM JOBS
GROUP BY JOB_ID;

-- Show the names of Departments which doesn’t have any employees

SELECT DEPARTMENTS.DEPARTMENT_NAME
FROM DEPARTMENTS
               LEFT JOIN EMPLOYEES 
                       ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
WHERE EMPLOYEES.DEPARTMENT_ID IS NULL;











  