USE phitron;

CREATE table Student
(
    Roll CHAR(4) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(50) UNIQUE,
    Address VARCHAR(250) ,
    Age INT CHECK(Age > 10)
);

INSERT into Student
(
   Roll,Name,email,Address,Age
)
values(1,'Rijuan','abc@gmail.com','ctg',12);

CREATE TABLE Student
(
    Roll CHAR(4),
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Address VARCHAR(250),
    Age INT,
    PRIMARY KEY (Roll),
    UNIQUE(Email),
    CHECK (Age > 10 )
);

CREATE TABLE Student
(
    Roll CHAR(4),
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(50),
    Address VARCHAR(250),
    Age INT,
    constraint PRIMARY KEY (Roll),
    constraint UNIQUE (Email),
    constraint CHECK (Age > 10 )
);


CREATE table libray
(
   bookname VARCHAR(50) PRIMARY KEY,
   who_hired_roll CHAR(4),
   Foreign Key (who_hired_roll) references Student(Roll)
);