CREATE DATABASE assignment;

USE assignment;

CREATE TABLE Student
( 
    S_ID INT PRIMARY KEY,
    S_NAME VARCHAR(50) NOT NULL,
    S_ADDRESS VARCHAR(50) 
);


CREATE TABLE Library
( 
    BOOK_ID INT PRIMARY KEY,
    BOOK_NAME VARCHAR(50) NOT NULL,
    S_ID INT,
    FOREIGN KEY (S_ID) references Student(S_ID)
);

CREATE TABLE Fess_table
( 
    FEE_ID INT PRIMARY KEY,
    FEES FLOAT NOT NULL,
    S_ID INT,
    FOREIGN KEY (S_ID) references Student(S_ID)
);