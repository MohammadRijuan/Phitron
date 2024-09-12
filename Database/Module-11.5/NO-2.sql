USE PRACTICES;

-- Insert a new borrowing record for a student (e.g., StudentID 3) for a book with the most available copies.

INSERT INTO BORROWING
(STUDENTID, ISBN, BORROWDATE, DUEDATE, RETURNDATE)
                                             SELECT 3,ISBN,CURDATE(),'2024-06-23','2024-06-23'
                                             FROM BOOK
                                             ORDER BY AVAILABLECOPIES DESC
                                             LIMIT 1;