CREATE DATABASE PRACTICES;

USE PRACTICES;

CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone VARCHAR(15),
    Address TEXT
);

CREATE TABLE Book (
    ISBN VARCHAR(13) PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Genre VARCHAR(50),
    TotalCopies INT NOT NULL,
    AvailableCopies INT NOT NULL
);

CREATE TABLE Borrowing (
    BorrowID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    ISBN VARCHAR(13),
    BorrowDate DATE NOT NULL,
    DueDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);

INSERT INTO STUDENT
(STUDENTID,NAME,EMAIL,PHONE,ADDRESS) VALUES (1,'RIJUAN','abc@gmail.com',123,'CTG'),
											(2,'MONJU','abcd@gmail.com',1234,'DHAKA'),
                                            (3,'sifat','abcde@gmail.com',12345,'SYLHET'),
                                            (4,'NIBRAJ','abcdef@gmail.com',123456,'CUMILLA');
                                            

INSERT INTO BOOK
(ISBN, TITLE, AUTHOR, GENRE, TOTALCOPIES, AVAILABLECOPIES) 
                                    VALUES("9780140430720", "HARRY POTTER", "RIJUAN", "GHOST", 2020, 270),
										  ("9780192823787", "SCIENCE FICTION", "JAFAR IQBAL", "SCIENCE", 5150, 570),
                                          ("9780545791879", "PATHAN", "MODHU", "TRILLER", 11000, 250);
INSERT INTO BOOK
(ISBN, TITLE, AUTHOR, GENRE, TOTALCOPIES, AVAILABLECOPIES) 
                                    VALUES("9781234567890", "XYZ", "KING", "ACTION", 2150, 300);
                                          
                                          
INSERT INTO BORROWING
(BORROWID, STUDENTID, ISBN, BORROWDATE, DUEDATE, RETURNDATE) 
                                    VALUES(1, 3, '9780192823787', CURDATE(), '2024-06-17','2024-06-15'), 
                                          (2, 3, '9780545791879', CURDATE(), '2024-06-17','2024-06-15'),
										  (3, 3, '9780140430720', CURDATE(), '2024-06-17','2024-06-15'),
                                          (4, 1, '9780140430720', '2024-06-16', '2024-06-23','2024-06-19'),
                                          (5, 2, '9780192823787', '2024-06-16', '2024-06-23','2024-06-19'),
                                          (6, 1, '9780545791879', '2024-06-16', '2024-06-23','2024-06-19');
INSERT INTO BORROWING
(BORROWID, STUDENTID, ISBN, BORROWDATE, DUEDATE, RETURNDATE) 
                                    VALUES(8, 3, '9781234567890', CURDATE(), '2024-06-17','2024-06-15'),
                                          (9, 3, '9781234567890', CURDATE(), '2024-06-17','2024-06-15'),
                                          (10, 2, '9781234567890', CURDATE(), '2024-06-17','2024-06-15'),
                                          (11, 3, '9781234567890', CURDATE(), '2024-06-17','2024-06-15');
                                          


