/*
CS373: Quiz #33 (5 pts) <Prateek>
*/

create table Student (sID   int,  sName text,    GPA        float, sizeHS   int);
create table Apply   (sID   int,  cName text,    major      text,  decision boolean);
create table College (cName text, state char(2), enrollment int);

/* -----------------------------------------------------------------------
 1. Get colleges with fewer than 5 applications and include the number of
    applications.
    (2 pts)
*/

select cName, count(*)
    from Apply
    group by cName
    having count(*) < 5;

/* -----------------------------------------------------------------------
 2. Get colleges with fewer than 5 applicants and include the number of
 	applicants.
    (2 pts)
*/

select cName, count(distinct sID)
    from Apply
    group by cName
    having count(distinct sID) < 5;
