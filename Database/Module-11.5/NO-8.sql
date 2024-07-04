-- There is a table named Employee. In that table there is a field named Salary. Determine the second lowest salary.

SELECT *
FROM EMPLOYEE
WHERE SALARY =(SELECT MIN(SALARY)
              FROM EMPLOYEE
			  WHERE SALARY > (SELECT MIN(SALARY)
                              FROM EMPLOYEE)
			 );