# Ankit Bansal Complex SQL Playlist  
(link - https://youtube.com/playlist?list=PLBTZqjSKn0IeKBQDjLmzisazhqQy4iGkb&si=FvqEB_MTceoJ_8KF)  
SQL Practice Ground - https://sqliteonline.com/

------------------------------------------------------------------------------------------------------------------------------------------------------
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
------------------------------------------------------------------------------------------------------------------------------------------------------
**2. Find new and repeat customers**

CREATE TABLE customer_orders (. 
    order_id INTEGER,
    customer_id INTEGER,  
    order_date TEXT,  
    order_amount INTEGER);   

INSERT INTO customer_orders 
VALUES  
(1,100,'2022-01-01',2000),  
(2,200,'2022-01-01',2500),  
(3,300,'2022-01-01',2100),  
(4,100,'2022-01-02',2000),  
(5,400,'2022-01-02',2200),  
(6,500,'2022-01-02',2700),  
(7,100,'2022-01-03',3000),  
(8,400,'2022-01-03',1000),  
(9,600,'2022-01-03',3000);  


```
WITH base AS
(
SELECT customer_id, MIN(order_date) AS first_order_date
FROM customer_orders
GROUP BY customer_id
  )

 SELECT ca.order_date,
        COUNT(CASE WHEN ca.order_date = b.first_order_date THEN ca.customer_id END) AS new_customers,
        COUNT(CASE WHEN ca.order_date != b.first_order_date THEN ca.customer_id END) AS repeat_customers
 FROM base b 
 JOIN customer_orders ca ON b.customer_id = ca.customer_id
 GROUP BY ca.order_date
```


| order_date   | new_customers  | repeat_customers |
| :---         |     :---:      |          ---:    |
| 2022-01-01   |     3          |          0       |
| 2022-01-02   |       2        |           1      |
| 2022-01-03   |      1         |           2       |




------------------------------------------------------------------------------------------------------------------------------------------------------

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
WITH base AS (
SELECT name, 
       floor,
       count(1) AS visits,
       ROW_NUMBER() OVER(Partition by name ORDER by count(1) DESC) AS rank_
from entries
GROUP BY name, floor
)


SELECT 
      entries.name, 
      COUNT(1) AS total_visits,
      max(case when rank_ = 1 then entries.floor end) AS most_visited_floor,
      --string_agg(resources, ', ') AS resources_used
      REPLACE(GROUP_CONCAT(DISTINCT entries.resources),',', ', ') AS resources_used

FROM entries 
join base on entries.name = base.name
         AND entries.floor = base.floor

GROUP by entries.name

```
Usage of **GROUP_CONCAT** is here <ins>so we can aggregate string characters and can pick unique items.</ins>

| Name | Total Visits | Most Visited Floor | Resources Used |
|------|-------------:|-------------------:|----------------|
| A    | 3            | 1                  | CPU, DESKTOP   |
| B    | 3            | 2                  | DESKTOP, MONITOR |

------------------------------------------------------------------------------------------------------------------------------------------------------
**4. Write a query to provide the nth occurence of Sunday in future from given date.**

```

selecrt

gg

```





















