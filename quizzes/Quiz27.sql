/*
CS373: Quiz #27 (5 pts) <Prateek>
*/

/* -----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

A B C
1 4 5
1 4 6
2 5 8
*/

create table R (A int, B int);
create table S (A int, B int, C int);

insert into R values (1, 4);
insert into R values (2, 5);
insert into R values (3, 6);

insert into S values (1, 3, 4);
insert into S values (1, 4, 5);
insert into S values (1, 4, 6);
insert into S values (2, 4, 7);
insert into S values (2, 5, 8);
insert into S values (3, 7, 9);

select *  from R natural join S;
