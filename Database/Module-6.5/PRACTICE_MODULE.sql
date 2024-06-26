USE DUMMYDB;

-- WAY-1 OF GETTING THIRD HIGHEST SALARY
SELECT MAX(SALARY)
FROM EMPLOYEES
WHERE SALARY < (SELECT MAX(SALARY)
                 FROM EMPLOYEES
                 WHERE SALARY < (SELECT MAX(SALARY)
                                  FROM EMPLOYEES
								  WHERE SALARY)
				);

-- WAY-2 NOW I HAVE TO ENSURE WHO WILL GET THOSE 2ND HIGHEST SALARY

SELECT *
FROM EMPLOYEES
WHERE SALARY = (SELECT DISTINCT SALARY
                FROM EMPLOYEES
                ORDER BY SALARY DESC
                LIMIT 1
                OFFSET 2);
                

-- LOWEST SALARY

SELECT MIN(SALARY)
FROM EMPLOYEES
WHERE SALARY > (SELECT MIN(SALARY)
                 FROM EMPLOYEES
                 WHERE SALARY > (SELECT MIN(SALARY)
                                  FROM EMPLOYEES
								  WHERE SALARY)
				);
                
SELECT *
FROM EMPLOYEES
WHERE SALARY = (SELECT DISTINCT SALARY
                FROM EMPLOYEES
                ORDER BY SALARY ASC
                LIMIT 1
                OFFSET 2);
                
                
SELECT *
FROM EMPLOYEES;
    
-- WHO HAS BEEN HIRED AFTER STEVEN

SELECT *
FROM EMPLOYEES
WHERE HIRE_DATE
order by HIRE_DATE ASC;

SELECT *
FROM EMPLOYEES
WHERE HIRE_DATE > (SELECT HIRE_DATE
                   FROM EMPLOYEES
                   WHERE FIRST_NAME='STEVEN'
                   ORDER BY HIRE_DATE ASC
                   LIMIT 1)
ORDER BY HIRE_DATE ASC;


-- USING CTE=COMMON TABLE EXPRESSION TO FINDOUT THIRD HIGHEST SALARY

-- WAY-1
WITH TEMP1 AS
(
SELECT *
FROM EMPLOYEES 
WHERE SALARY = (SELECT DISTINCT SALARY 
                FROM EMPLOYEES
                ORDER BY SALARY DESC
                LIMIT 1
                OFFSET 2)
)
SELECT *
FROM TEMP1;

-- WAY-2
WITH RANK_SALARY AS
(
	SELECT  FIRST_NAME,SALARY,
		(SELECT COUNT(DISTINCT(SALARY)) FROM EMPLOYEES E2 WHERE E2.SALARY > E1.SALARY)+1 AS SALARY_RANK_DESC 
    FROM EMPLOYEES E1
    )

SELECT *
FROM RANK_SALARY
WHERE SALARY_RANK_DESC=3
 LIMIT 1;
 
 
 -- LOWEST 3RD HIGHEST SALARY USING CTE
WITH TEMP2 AS
(
SELECT *
FROM EMPLOYEES 
WHERE SALARY = (SELECT DISTINCT SALARY 
                FROM EMPLOYEES
                ORDER BY SALARY ASC
                LIMIT 1
                OFFSET 2)
)
SELECT *
FROM TEMP2;






                









                
                