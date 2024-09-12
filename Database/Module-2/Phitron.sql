CREATE Database Phitron;

Use Phitron;

CREATE TABLE student(
   Roll char(4) primary key,
   Name varchar(50),
   marks Double
);
   
INSERT into student
(Roll,Name,marks) values (1,'Rijuan', 99) 

INSERT into student
(Roll,Name) values (2,'Monju') 

INSERT into student
(Roll,Name,marks) values (1,'Rijuan', 99) 

SET SQL_SAFE_UPDATES =0;
UPDATE student
SET Name= 'Sifat'
WHERE Name= 'Rijuan' ;
SET SQL_SAFE_UPDATES =1;

DELETE from student
Where Roll=1
