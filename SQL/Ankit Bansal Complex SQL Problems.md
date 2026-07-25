# Ankit Bansal Complex SQL Playlist  
(link - https://youtube.com/playlist?list=PLBTZqjSKn0IeKBQDjLmzisazhqQy4iGkb&si=FvqEB_MTceoJ_8KF)  
SQL Practice Ground - https://sqliteonline.com/


**1. Complex SQL Query 1 | Derive Points table for ICC tournament**

create table icc_world_cup
(
Team_1 Varchar(20),  
Team_2 Varchar(20),  
Winner Varchar(20)  
);  
INSERT INTO icc_world_cup values('India','SL','India');  
INSERT INTO icc_world_cup values('SL','Aus','Aus');  
INSERT INTO icc_world_cup values('SA','Eng','Eng');  
INSERT INTO icc_world_cup values('Eng','NZ','NZ');  
INSERT INTO icc_world_cup values('Aus','India','India');  

select * from icc_world_cup;


```
with base as (
select team_1 AS team,
       CAse when team_1 = winner then 1 else 0 end as win_flag

from icc_world_cup

UNION ALL

SELECT team_2 AS team, 
       CAse when team_2 = winner then 1 else 0 end as win_flag

FROM icc_world_cup
  )
  
  select team, 
         COUNT(1) AS matches_played,
         SUM(win_flag) AS matches_won,
         COUNT(1) - SUM(win_flag) AS matches_lost
  
  from base
  GROUP BY team
```

**2. Find new and repeat customers**

create table customer_orders (  
order_id integer,  
customer_id integer,  
order_date date,  
order_amount integer  
);  
select * from customer_orders  ;
insert into customer_orders values(1,100,cast('2022-01-01' as date),2000),(2,200,cast('2022-01-01' as date),2500),(3,300,cast('2022-01-01' as date),2100)  
,(4,100,cast('2022-01-02' as date),2000),(5,400,cast('2022-01-02' as date),2200),(6,500,cast('2022-01-02' as date),2700)  
,(7,100,cast('2022-01-03' as date),3000),(8,400,cast('2022-01-03' as date),1000),(9,600,cast('2022-01-03' as date),3000);  


```
SELECT *


```




**3. Scenario based Interviews Question for Product companies**

create table entries (   
name varchar(20),  
address varchar(20),  
email varchar(20),  
floor int,  
resources varchar(10));  

insert into entries   
values ('A','Bangalore','A@gmail.com',1,'CPU'),('A','Bangalore','A1@gmail.com',1,'CPU'),('A','Bangalore','A2@gmail.com',2,'DESKTOP')  
,('B','Bangalore','B@gmail.com',2,'DESKTOP'),('B','Bangalore','B1@gmail.com',2,'DESKTOP'),('B','Bangalore','B2@gmail.com',1,'MONITOR')  




```
SELECT *

```


**4. Write a query to provide the nth occurence of Sunday in future from given date.**

```

selecrt

gg

```





















