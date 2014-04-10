use downing_test;

/* -----------------------------------------------------------------------
Joins
http://i.stack.imgur.com/1UKp7.png
*/

# ------------------------------------------------------------------------
select "Drop";

drop table if exists R;
drop table if exists S;

# ------------------------------------------------------------------------
select "";
select "Create";

create table R (A int);
create table S (B int, C int);

# ------------------------------------------------------------------------
select "";
select "Insert";

insert into R values (1);
insert into R values (2);
insert into R values (3);

insert into S values (1, 6);
insert into S values (1, 7);
insert into S values (4, 8);
insert into S values (4, 9);

# ------------------------------------------------------------------------
select "";
select "Cross Join";
select * from R;
select * from S;

# select count(*) from R, S;
# select       *  from R, S;

select count(*) from R cross join S;
select       *  from R cross join S;

# select count(*) from R inner join S;
# select       *  from R inner join S;

# ------------------------------------------------------------------------
select "";
select "Theta Join";
select * from R;
select * from S;

# select count(*) from R, S where R.A = S.B;
# select       *  from R, S where R.A = S.B;

# select count(*) from R cross join S where R.A = S.B;
# select       *  from R cross join S where R.A = S.B;

# select count(*) from R inner join S where R.A = S.B;
# select       *  from R inner join S where R.A = S.B;

# select count(*) from R, S on R.A = S.B; # You have an error in your SQL syntax
# select       *  from R, S on R.A = S.B; # You have an error in your SQL syntax

# select count(*) from R cross join S on R.A = S.B;
# select       *  from R cross join S on R.A = S.B;

select count(*) from R inner join S on R.A = S.B;
select       *  from R inner join S on R.A = S.B;

# ------------------------------------------------------------------------
select "";
select "Left Join";
select * from R;
select * from S;

# select count(*) from R left join S; # You have an error in your SQL syntax
# select       *  from R left join S; # You have an error in your SQL syntax

# select count(*) from R left join S where R.A = S.B; # You have an error in your SQL syntax
# select       *  from R left join S where R.A = S.B; # You have an error in your SQL syntax

select count(*) from R left join S on R.A = S.B;
select       *  from R left join S on R.A = S.B;

# ------------------------------------------------------------------------
select "";
select "Right Join";
select * from R;
select * from S;

# select count(*) from R right join S; # You have an error in your SQL syntax
# select       *  from R right join S; # You have an error in your SQL syntax

# select count(*) from R right join S where R.A = S.B; # You have an error in your SQL syntax
# select       *  from R right join S where R.A = S.B; # You have an error in your SQL syntax

select count(*) from R right join S on R.A = S.B;
select       *  from R right join S on R.A = S.B;

# ------------------------------------------------------------------------
select "";
select "Natural Join";
select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

# ------------------------------------------------------------------------
select "";
select "Drop";

drop table if exists R;
drop table if exists S;

# ------------------------------------------------------------------------
select "";
select "Create";

create table R (A int);
create table S (A int, C int);

# ------------------------------------------------------------------------
select "";
select "Insert";

insert into R values (1);
insert into R values (2);
insert into R values (3);

insert into S values (6, 1);
insert into S values (7, 2);
insert into S values (8, 3);
insert into S values (9, 4);

# ------------------------------------------------------------------------
select "";
select "Cross Join";
select * from R;
select * from S;

# select count(*) from R, S;
# select       *  from R, S;

select count(*) from R cross join S;
select       *  from R cross join S;

# select count(*) from R inner join S;
# select       *  from R inner join S;

# ------------------------------------------------------------------------
select "";
select "Theta Join";
select * from R;
select * from S;

# select count(*) from R, S where R.A = S.A;
# select       *  from R, S where R.A = S.A;

# select count(*) from R cross join S where R.A = S.A;
# select       *  from R cross join S where R.A = S.A;

# select count(*) from R inner join S where R.A = S.A;
# select       *  from R inner join S where R.A = S.A;

# select count(*) from R, S on R.A = S.A; # You have an error in your SQL syntax
# select       *  from R, S on R.A = S.A; # You have an error in your SQL syntax

# select count(*) from R cross join S on R.A = S.A;
# select       *  from R cross join S on R.A = S.A;

# select count(*) from R inner join S on R.A = S.A;
# select       *  from R inner join S on R.A = S.A;

# select count(*) from R, S using (A); # You have an error in your SQL syntax
# select       *  from R, S using (A); # You have an error in your SQL syntax

# select count(*) from R cross join S using (A);
# select       *  from R cross join S using (A);

select count(*) from R inner join S using (A);
select       *  from R inner join S using (A);

# ------------------------------------------------------------------------
select "";
select "Left Join";
select * from R;
select * from S;

# select count(*) from R left join S; # You have an error in your SQL syntax
# select       *  from R left join S; # You have an error in your SQL syntax

# select count(*) from R left join S where R.A = S.A; # You have an error in your SQL syntax
# select       *  from R left join S where R.A = S.A; # You have an error in your SQL syntax

select count(*) from R left join S on R.A = S.A;
select       *  from R left join S on R.A = S.A;

select count(*) from R left join S using (A);
select       *  from R left join S using (A);

# ------------------------------------------------------------------------
select "";
select "Right Join";
select * from R;
select * from S;

# select count(*) from R right join S; # You have an error in your SQL syntax
# select       *  from R right join S; # You have an error in your SQL syntax

# select count(*) from R right join S where R.A = S.A; # You have an error in your SQL syntax
# select       *  from R right join S where R.A = S.A; # You have an error in your SQL syntax

select count(*) from R right join S on R.A = S.A;
select       *  from R right join S on R.A = S.A;

select count(*) from R right join S using (A);
select       *  from R right join S using (A);

# ------------------------------------------------------------------------
select "";
select "Natural Join";
select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

# ------------------------------------------------------------------------
select "";
select "Drop";

drop table if exists R;
drop table if exists S;

# ------------------------------------------------------------------------
select "";
select "Create";

create table R (A int);
create table S (A int, C int);

# ------------------------------------------------------------------------
select "";
select "Insert";

insert into R values (1);
insert into R values (2);
insert into R values (3);

insert into S values (1, 6);
insert into S values (1, 7);
insert into S values (4, 8);
insert into S values (4, 9);

# ------------------------------------------------------------------------
select "";
select "Cross Join";
select * from R;
select * from S;

# select count(*) from R, S;
# select       *  from R, S;

select count(*) from R cross join S;
select       *  from R cross join S;

# select count(*) from R inner join S;
# select       *  from R inner join S;

# ------------------------------------------------------------------------
select "";
select "Theta Join";
select * from R;
select * from S;

# select count(*) from R, S where R.A = S.A;
# select       *  from R, S where R.A = S.A;

# select count(*) from R cross join S where R.A = S.A;
# select       *  from R cross join S where R.A = S.A;

# select count(*) from R inner join S where R.A = S.A;
# select       *  from R inner join S where R.A = S.A;

# select count(*) from R, S on R.A = S.A; # You have an error in your SQL syntax
# select       *  from R, S on R.A = S.A; # You have an error in your SQL syntax

# select count(*) from R cross join S on R.A = S.A;
# select       *  from R cross join S on R.A = S.A;

# select count(*) from R inner join S on R.A = S.A;
# select       *  from R inner join S on R.A = S.A;

# select count(*) from R, S using (A); # You have an error in your SQL syntax
# select       *  from R, S using (A); # You have an error in your SQL syntax

# select count(*) from R cross join S using (A);
# select       *  from R cross join S using (A);

select count(*) from R inner join S using (A);
select       *  from R inner join S using (A);

# ------------------------------------------------------------------------
select "";
select "Left Join";
select * from R;
select * from S;

# select count(*) from R left join S; # You have an error in your SQL syntax
# select       *  from R left join S; # You have an error in your SQL syntax

# select count(*) from R left join S where R.A = S.A; # You have an error in your SQL syntax
# select       *  from R left join S where R.A = S.A; # You have an error in your SQL syntax

select count(*) from R left join S on R.A = S.A;
select       *  from R left join S on R.A = S.A;

select count(*) from R left join S using (A);
select       *  from R left join S using (A);

# ------------------------------------------------------------------------
select "";
select "Right Join";
select * from R;
select * from S;

# select count(*) from R right join S; # You have an error in your SQL syntax
# select       *  from R right join S; # You have an error in your SQL syntax

# select count(*) from R right join S where R.A = S.A; # You have an error in your SQL syntax
# select       *  from R right join S where R.A = S.A; # You have an error in your SQL syntax

select count(*) from R right join S on R.A = S.A;
select       *  from R right join S on R.A = S.A;

select count(*) from R right join S using (A);
select       *  from R right join S using (A);

# ------------------------------------------------------------------------
select "";
select "Natural Join";
select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

# ------------------------------------------------------------------------
select "";
select "Drop";

drop table if exists R;
drop table if exists S;

# ------------------------------------------------------------------------
select "";
select "Create";

create table R (A int, B int);
create table S (A int, B int, C int);

# ------------------------------------------------------------------------
select "";
select "Insert";

insert into R values (1, 4);
insert into R values (2, 5);
insert into R values (3, 6);

insert into S values (1, 3, 4);
insert into S values (1, 4, 5);
insert into S values (1, 4, 6);
insert into S values (2, 4, 7);
insert into S values (2, 5, 8);
insert into S values (3, 7, 9);

# ------------------------------------------------------------------------
select "";
select "Cross Join";
select * from R;
select * from S;

# select count(*) from R, S;
# select       *  from R, S;

select count(*) from R cross join S;
select       *  from R cross join S;

# select count(*) from R inner join S;
# select       *  from R inner join S;

# ------------------------------------------------------------------------
select "";
select "Theta Join";
select * from R;
select * from S;

# select count(*) from R, S where R.A = S.A and R.B = S.B;
# select       *  from R, S where R.A = S.A and R.B = S.B;

# select count(*) from R cross join S where R.A = S.A and R.B = S.B;
# select       *  from R cross join S where R.A = S.A and R.B = S.B;

# select count(*) from R inner join S where R.A = S.A and R.B = S.B;
# select       *  from R inner join S where R.A = S.A and R.B = S.B;

# select count(*) from R, S on R.A = S.A and R.B = S.B; # You have an error in your SQL syntax
# select       *  from R, S on R.A = S.A and R.B = S.B; # You have an error in your SQL syntax

# select count(*) from R cross join S on R.A = S.A and R.B = S.B;
# select       *  from R cross join S on R.A = S.A and R.B = S.B;

select count(*) from R inner join S on R.A = S.A and R.B = S.B;
select       *  from R inner join S on R.A = S.A and R.B = S.B;

# ------------------------------------------------------------------------
select "";
select "Left Join";
select * from R;
select * from S;

# select count(*) from R left join S; # You have an error in your SQL syntax
# select       *  from R left join S; # You have an error in your SQL syntax

# select count(*) from R left join S where R.A = S.A and R.B = S.B; # You have an error in your SQL syntax
# select       *  from R left join S where R.A = S.A and R.B = S.B; # You have an error in your SQL syntax

select count(*) from R left join S on R.A = S.A and R.B = S.B;
select       *  from R left join S on R.A = S.A and R.B = S.B;

# ------------------------------------------------------------------------
select "";
select "Right Join";
select * from R;
select * from S;

# select count(*) from R right join S; # You have an error in your SQL syntax
# select       *  from R right join S; # You have an error in your SQL syntax

# select count(*) from R right join S where R.A = S.A and R.B = S.B; # You have an error in your SQL syntax
# select       *  from R right join S where R.A = S.A and R.B = S.B; # You have an error in your SQL syntax

select count(*) from R right join S on R.A = S.A and R.B = S.B;
select       *  from R right join S on R.A = S.A and R.B = S.B;

# ------------------------------------------------------------------------
select "";
select "Natural Join";
select * from R;
select * from S;

select count(*) from R natural join S;
select       *  from R natural join S;

# ------------------------------------------------------------------------
select "";
select "Drop";

drop table if exists R;
drop table if exists S;
drop table if exists T;

# ------------------------------------------------------------------------
select "";
select "Create";

create table T (A int);

# ------------------------------------------------------------------------
select "";
select "Insert";

insert into T values (1);
insert into T values (2);
insert into T values (3);

# ------------------------------------------------------------------------
select "";
select "Cross Join";
select * from T;

# select count(*) from T as R, T as S;
# select       *  from T as R, T as S;

select count(*) from T as R cross join T as S;
select       *  from T as R cross join T as S;

# select count(*) from T as R inner join T as S;
# select       *  from T as R inner join T as S;

# ------------------------------------------------------------------------
select "";
select "Theta Join";
select * from T;

# select count(*) from T as R, T as S where R.A = S.A;
# select       *  from T as R, T as S where R.A = S.A;

# select count(*) from T as R cross join T as S where R.A = S.A;
# select       *  from T as R cross join T as S where R.A = S.A;

# select count(*) from T as R inner join T as S where R.A = S.A;
# select       *  from T as R inner join T as S where R.A = S.A;

# select count(*) from T as R, T as S on R.A = S.A; # You have an error in your SQL syntax
# select       *  from T as R, T as S on R.A = S.A; # You have an error in your SQL syntax

# select count(*) from T as R cross join T as S on R.A = S.A;
# select       *  from T as R cross join T as S on R.A = S.A;

# select count(*) from T as R inner join T as S on R.A = S.A;
# select       *  from T as R inner join T as S on R.A = S.A;

# select count(*) from T as R, T as S using (A); # You have an error in your SQL syntax
# select       *  from T as R, T as S using (A); # You have an error in your SQL syntax

# select count(*) from T as R cross join T as S using (A);
# select       *  from T as R cross join T as S using (A);

select count(*) from T as R inner join T as S using (A);
select       *  from T as R inner join T as S using (A);

# ------------------------------------------------------------------------
select "";
select "Left Join";
select * from T;

# select count(*) from T as R left join T as S; # You have an error in your SQL syntax
# select       *  from T as R left join T as S; # You have an error in your SQL syntax

# select count(*) from T as R left join T as S where R.A = S.A; # You have an error in your SQL syntax
# select       *  from T as R left join T as S where R.A = S.A; # You have an error in your SQL syntax

select count(*) from T as R left join T as S on R.A = S.A;
select       *  from T as R left join T as S on R.A = S.A;

select count(*) from T as R left join T as S using (A);
select       *  from T as R left join T as S using (A);

# ------------------------------------------------------------------------
select "";
select "Right Join";
select * from T;

# select count(*) from T as R right join T as S; # You have an error in your SQL syntax
# select       *  from T as R right join T as S; # You have an error in your SQL syntax

# select count(*) from T as R right join T as S where R.A = S.A; # You have an error in your SQL syntax
# select       *  from T as R right join T as S where R.A = S.A; # You have an error in your SQL syntax

select count(*) from T as R right join T as S on R.A = S.A;
select       *  from T as R right join T as S on R.A = S.A;

select count(*) from T as R right join T as S using (A);
select       *  from T as R right join T as S using (A);

# ------------------------------------------------------------------------
select "";
select "Natural Join";
select * from T;

select count(*) from T as R natural join T as S;
select       *  from T as R natural join T as S;

# ------------------------------------------------------------------------
select "";
select "Drop";

drop table if exists T;

exit
