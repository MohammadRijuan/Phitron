USE assignment;

CREATE table  EMPLOYEE
(
    EMPLOYEE_ID INT PRIMARY KEY,
    FIRST_NAME VARCHAR(50) UNIQUE,
    LAST_NAME VARCHAR(50) NOT NULL,
    AGE INT ,
    DEPARTMENT VARCHAR(50) NOT NULL
);

INSERT INTO EMPLOYEE
(EMPLOYEE_ID,FIRST_NAME,LAST_NAME,AGE,DEPARTMENT)  VALUES (1,'JOHN','DOE',28,'SALES'),
														  (2,'JANE','SMITH',32,'MARKETING'),
                                                          (3,'MICHAEL','JHONSON',35,'FINANCE'),
                                                          (4,'SARAH','BROWN',30,'HR'),
                                                          (5,'WILLIAM','DAVIS',25,'ENGINEERING'),
                                                          (6,'EMILY','WILSON',28,'SALES'),
                                                          (7,'ROBERT','LEE',33,'MARKETING'),
                                                          (8,'LAURA','HALL',29,'FINANCE'),
                                                          (9,'THOMAS','WHITE',31,'HR'),
                                                          (10,'OLIVIA','CLARK',27,'ENGINEERING');
                                                          
														
                                                        
SELECT * FROM EMPLOYEE
WHERE FIRST_NAME LIKE '%SON%' OR LAST_NAME LIKE '%SON%';