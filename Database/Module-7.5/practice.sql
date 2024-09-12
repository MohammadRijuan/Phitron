USE DUMMYDB;

-- Show the employee names and corresponding job_titles without using JOIN query

SELECT *
FROM EMPLOYEES;

SELECT EMPLOYEES.FIRST_NAME, JOBS.JOB_TITLE
FROM EMPLOYEES ,JOBS
WHERE EMPLOYEES.JOB_ID = JOBS.JOB_ID;

-- Do the question no 1 using JOIN query

SELECT EMPLOYEES.FIRST_NAME , JOBS.JOB_TITLE
FROM EMPLOYEES 
            INNER JOIN JOBS
                 ON EMPLOYEES.JOB_ID =JOBS.JOB_ID;
                 
-- Show the name of the employee and the job_title who receives the maximum salary

SELECT EMPLOYEES.FIRST_NAME , JOBS.JOB_TITLE,SALARY
FROM EMPLOYEES 
            JOIN JOBS
                ON EMPLOYEES.JOB_ID= JOBS.JOB_ID
WHERE SALARY = (SELECT MAX(SALARY) FROM EMPLOYEES);

-- Show the list of employee name and corresponding manager names.

SELECT E.FIRST_NAME AS EMPLOYEE ,M.FIRST_NAME AS MANAGER
FROM EMPLOYEES AS E 
                 JOIN EMPLOYEES AS M
                     ON E.MANAGER_ID = M.EMPLOYEE_ID;


