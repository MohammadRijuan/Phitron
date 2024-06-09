"""
***Primary key->

A Primary Key is a unique identifier for a record in a database table. It ensures that each record can be uniquely identified and no two records can have the same primary key value. The primary key must contain unique values, and it cannot contain NULL values.

Example:

Consider a table Students:

StudentID	FirstName	LastName	Age
1	        John	     Doe	    20
2	        Jane	     Smith	    22
3	        Jim	         Brown	    21
In this table, StudentID is the primary key. Each StudentID value is unique and not NULL, ensuring that each student record can be uniquely identified.


***Composite key->

A Composite Primary Key is a primary key composed of two or more columns. It is used when a single column is not sufficient to uniquely identify a record.

Example:

Consider a table Enrollments that records which students are enrolled in which courses:

StudentID	CourseID	EnrollmentDate
1	        101	        2023-01-15
1	        102	        2023-02-15
2	        101	        2023-01-15
In this table, the combination of StudentID and CourseID is used as the composite primary key. This combination ensures that each record is unique, as a student cannot be enrolled in the same course more than once on the same date.


***Foreign key->

A Foreign Key is a field (or a collection of fields) in one table that uniquely identifies a row of another table or the same table. The foreign key is defined in a second table, but it refers to the primary key or a unique key in the first table. It establishes a relationship between the records in the two tables.

Example:

Consider two tables, Students and Enrollments:

Students:

StudentID	FirstName	LastName	Age
1	        John	     Doe	    20
2	        Jane	     Smith	    22
3	        Jim	         Brown	    21
Enrollments:

EnrollmentID	StudentID	CourseID	EnrollmentDate
1	             1	          101	     2023-01-15
2	             1	          102	     2023-02-15
3	             2	          101	     2023-01-15
In the Enrollments table, StudentID is a foreign key that references the StudentID in the Students table. This relationship ensures that each enrollment record corresponds to a valid student.

By defining StudentID in the Enrollments table as a foreign key, we ensure referential integrity, meaning that a student must exist in the Students table for an enrollment record to be valid. This prevents the insertion of an enrollment record with a StudentID that does not exist in the Students table.


"""