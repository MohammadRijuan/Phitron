CREATE DATABASE practice;

USE practice;

CREATE TABLE Employee
(
    ID CHAR(4) PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(50) UNIQUE,
    PHONE INT UNIQUE
);

INSERT INTO EMPLOYEE
(ID,NAME,EMAIL,PHONE) values 
(1,'RIJUAN','abc@gmail.com',123456),
(2,'MONJU','abcde@gmail.com',12345023);

SELECT * FROM Employee;

DELETE FROM EMPLOYEE WHERE ID='1';

SELECT * FROM Employee;



