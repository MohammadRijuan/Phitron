-- Retrieve the books that are overdue (i.e., the return date is before the current date).

USE PRACTICES;

SELECT B.TITLe
FROM BOOK AS B 
             JOIN BORROWING AS BR
                                ON B.ISBN =BR.ISBN
where BR.RETURNDATE < CURDATE();