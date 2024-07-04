-- There are tables named Employee, Job History, Department.
-- Use ON DELETE CASCADE on Job History for deleting Employee
-- Use ON DELETE SET NULL on Employee for deleting Department

CREATE TABLE DEPARTMENT
(  
     DEPT_ID CHAR(4) PRIMARY KEY,
     DEPT_NAME VARCHAR(50) NOT NULL
);

CREATE TABLE EMPLOYEE
(  
     EMP_ID CHAR(4) PRIMARY KEY,
     EMP_NAME VARCHAR(50) NOT NULL,
     EMP_ADDRESS VARCHAR(50) NOT NULL, 
     DEPT_ID CHAR(4),
     FOREIGN KEY (DEPT_ID) references DEPARTMENT(DEPT_ID) 
     ON DELETE SET NULL
);

CREATE TABLE JOB_HISTORY
(  
     EMP_ID CHAR(4),
     JOINING_DATE DATE,
     FOREIGN KEY (EMP_ID) references EMPLOYEE(EMP_ID) 
     ON DELETE CASCADE
);

