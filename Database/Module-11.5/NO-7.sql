-- Explain UNION and UNION ALL set operations in MySQL

-- UNION -> UNION OPERATIONS REMOVE ALL DUPLICATE ELEMENTS FROM THE TWO OR MORE THAN SET AND GIVES THE FINAL RESULT

CREATE TABLE STU1(
    STU_ID INT PRIMARY KEY,
    STU_NAME VARCHAR(50),
    STU_ADDRESS VARCHAR(50)

);

CREATE TABLE STU2(
    STU_ID INT PRIMARY KEY,
    STU_NAME VARCHAR(50),
    STU_ADDRESS VARCHAR(50)

);

SELECT *
FROM STU1
UNION
SELECT *
FROM STU2;


-- UNION ALL -> UNION OPERATIONS GIVES THE RESULT OF TWO SET INCLUDING DIFFERENT  AND DUPLICATE ELEMENT



CREATE TABLE STU1(
    STU_ID INT PRIMARY KEY,
    STU_NAME VARCHAR(50),
    STU_ADDRESS VARCHAR(50)

);

CREATE TABLE STU2(
    STU_ID INT PRIMARY KEY,
    STU_NAME VARCHAR(50),
    STU_ADDRESS VARCHAR(50)

);

SELECT *
FROM STU1
UNION ALL
SELECT *
FROM STU2;




