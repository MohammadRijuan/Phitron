-- Create a table named "employees" with the specified columns
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    salary DECIMAL(10, 2),
    join_date DATE,
    department VARCHAR(100)
);

-- Insert some sample data into the "employees" table
INSERT INTO employees (name, age, salary, join_date, department) VALUES
('John Doe', 30, 50000.00, '2023-01-15', 'Marketing'),
('Jane Smith', 25, 55000.00, '2022-07-20', 'Finance'),
('Bob Johnson', 35, 60000.00, '2022-09-10', 'Human Resources'),
('Emily Brown', 28, 52000.00, '2023-03-05', 'Operations');

-- function (MIN,MAX,COUNT,SUM,AVG) 
SELECT MAX(age)  FROM employees;



-- SQL GROUP BY Examples
-- GROUP BY Syntax
/*SELECT column_name(s)
FROM table_name
WHERE condition 
GROUP BY column_name(s)
ORDER BY column_name(s);*/

SELECT department, AVG(salary)
FROM EMPLOYEES 
GROUP BY department ;

SELECT department, AVG(salary)
FROM employees
WHERE department = 'Marketing'
GROUP BY department;

SELECT department, COUNT(*)
FROM employees
GROUP BY department;

-- SQL WHERE 
/*
SELECT column1, column2, ...
FROM table_name
WHERE condition;
*/

SELECT department, AVG(salary)
FROM employees
WHERE department = 'Marketing'

-- HAVING Syntax
/*SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);*/

SELECT department, AVG(salary) AS SAL
FROM employees
WHERE department != 'Marketing'
GROUP BY department
HAVING SAL<55000;


-- ALTER TABLE ( ADD Column,DROP COLUMN,RENAME COLUMN,ALTER/MODIFY DATATYPE etc)

ALTER TABLE employees 
ADD Registation_Num VARCHAR(200);

ALTER TABLE employees 
ADD EMAIL VARCHAR(200);

ALTER TABLE employees 
DROP EMAIL ;

ALTER TABLE employees 
MODIFY Registation_Num INT;

SELECT * FROM employees ;



