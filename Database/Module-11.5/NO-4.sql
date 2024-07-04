-- Retrieve the names of students who have borrowed the most books.

SELECT S.NAME
FROM STUDENT AS S
               JOIN BORROWING AS B
                               ON S.STUDENTID=B.STUDENTID
GROUP BY S.NAME
ORDER BY COUNT(B.BORROWID) DESC
LIMIT 1;