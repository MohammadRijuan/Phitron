-- Using Update Query, decrease the available copies of a book (e.g., ISBN '9781234567890') by 1 when a student borrows it.

UPDATE BOOK
SET AVAILABLECOPIES = AVAILABLECOPIES -1
WHERE ISBN = '9781234567890';
