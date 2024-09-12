CREATE DATABASE Practice;

USE Practice;

CREATE TABLE Student(
   Id  INT AUTO_INCREMENT PRIMARY KEY,
   Roll CHAR(4) ,
   Name VARCHAR(50) NOT NULL,
   Address VARCHAR(50)
);


INSERT INTO Student (Id,Roll, Name, Address) 
VALUES 
   (11,01, 'Rijuan', 'CTG'),
   (12,02, 'Monju', 'Dhaka'),
   (13,03, 'Sifat', 'Sylhet');
   
ALTER TABLE Student
ADD COLUMN Salary DECIMAL(10, 2);

SET SQL_SAFE_UPDATES=0;
UPDATE Student
SET Salary = 
    CASE 
        WHEN Name = 'Rijuan' THEN 120000
        WHEN Name = 'Monju' THEN 1130000
        WHEN Name = 'Sifat' THEN 140000
        ELSE Salary  -- This line ensures that existing salary for other records remain unchanged
    END
WHERE Name IN ('Rijuan', 'Monju', 'Sifat');
SET SQL_SAFE_UPDATES=1;

SELECT * 
FROM Student
WHERE SALARY > (SELECT SALARY 
                FROM Student
                WHERE ID=11);
                
ALTER TABLE STUDENT
ADD COLUMN DEPARTMENT VARCHAR(50);

SET SQL_SAFE_UPDATES=0;
UPDATE Student
SET DEPARTMENT = 
    CASE 
        WHEN Name = 'Rijuan' THEN 'SCIENCE'
        WHEN Name = 'Monju' THEN 'ARTS'
        WHEN Name = 'Sifat' THEN 'COMMERECE'
        ELSE Salary  -- This line ensures that existing salary for other records remain unchanged
    END
WHERE Name IN ('Rijuan', 'Monju', 'Sifat');
SET SQL_SAFE_UPDATES=1;

ALTER TABLE STUDENT
MODIFY SALARY DECIMAL(100,2);


DROP TABLE Student;
