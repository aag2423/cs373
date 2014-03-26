/*
CS373: Quiz #25 (5 pts) <Prateek>
*/

create table Student (sID   int,  sName text,    GPA        float, sizeHS   int);
create table Apply   (sID   int,  cName text,    major      text,  decision boolean);
create table College (cName text, state char(2), enrollment int);

/* -----------------------------------------------------------------------
 1. Write an SQL query to return the ID and name of all students who
    applied to Stanford in CS.
    (4 pts)
*/

select sID, sName
    from Student
    inner join Apply
    where (Student.sID = Apply.sID) and (cName = "Stanford") and (major = 'CS');

select sID, sName
    from Student
    inner join Apply on Student.sID = Apply.sID
    where (cName = "Stanford") and (major = 'CS');

select sID, sName
    from Student
    inner join Apply using (sID)
    where (cName = "Stanford") and (major = 'CS');

select sID, sName
    from Student
    natural join Apply
    where (cName = "Stanford") and (major = 'CS');
