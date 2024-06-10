use assignment;

CREATE TABLE Student
(
    ID INT PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL,
    ADDRESS VARCHAR(500)
);

INSERT INTO Student
(ID,NAME,ADDRESS) VALUES (01,'RIJUAN','CTG'),
                         (02,'MONJU','DHAKA'),
                         (03,'SIFAT','COMILLA');
                         
						
					
SET SQL_SAFE_UPDATES=0;
UPDATE Student SET NAME='NIBRAJ' WHERE NAME='RIJUAN';
DELETE FROM Student WHERE ID=02;
SET SQL_SAFE_UPDATES=1;
