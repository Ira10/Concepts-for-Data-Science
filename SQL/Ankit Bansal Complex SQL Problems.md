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

SELECT strftime('%w', 'now');   -- TRIED ON 25TH OCT '26, COME BACK TO THIS AGAIN


```
------------------------------------------------------------------------------------------------------------------------------------------------------

**5. Pareto Principle (80/20 Rule), 80% of the sales comes from 20% of the product.**
-- 25th Oct -- 30 mins --

DROP TABLE IF EXISTS sales;  
DROP TABLE IF EXISTS products;  

CREATE TABLE products (
  product_id   INTEGER PRIMARY KEY,
  product_name TEXT,
  unit_price   REAL
);  

CREATE TABLE sales (
  sale_id    INTEGER PRIMARY KEY,
  product_id INTEGER,
  sale_date  TEXT,
  qty        INTEGER
);  

INSERT INTO products VALUES  
(1,'Laptop',800),(2,'Smartphone',600),(3,'Monitor',250),(4,'Headphones',120),  
(5,'Mouse',15),(6,'Keyboard',30),(7,'USB Cable',5),(8,'Webcam',40),  
(9,'Mousepad',8),(10,'Charger',12),(11,'Phone Case',10),(12,'Screen Cleaner',6),  
(13,'Laptop Stand',25),(14,'HDMI Cable',9),(15,'Flash Drive',11),(16,'SD Card',14),  
(17,'Stylus',18),(18,'Sticker Pack',3),(19,'Cable Ties',4),(20,'Batteries',7);  

INSERT INTO sales VALUES  
(1,1,'2026-01-10',10),(2,1,'2026-02-12',8),(3,1,'2026-03-15',12),  
(4,2,'2026-01-05',15),(5,2,'2026-02-08',12),(6,2,'2026-03-20',14),  
(7,3,'2026-01-18',20),(8,3,'2026-02-22',15),(9,3,'2026-03-09',15),  
(10,4,'2026-01-25',40),(11,4,'2026-02-14',30),(12,4,'2026-03-28',30),  
(13,5,'2026-01-11',120),(14,6,'2026-01-19',60),(15,7,'2026-01-23',300),  
(16,8,'2026-02-02',40),(17,9,'2026-02-09',150),(18,10,'2026-02-16',120),  
(19,11,'2026-02-20',150),(20,12,'2026-02-25',150),(21,13,'2026-03-03',40),  
(22,14,'2026-03-07',100),(23,15,'2026-03-12',80),(24,16,'2026-03-18',60),  
(25,17,'2026-03-22',40),(26,18,'2026-03-26',200),(27,19,'2026-03-29',150),  
(28,20,'2026-03-30',100);  


```

with base as (
SELECT product_name, sum(unit_price * qty) as sales,
       SUM(SUM(unit_price * qty)) OVER() AS grand_total_sales,
       SUM(sum(unit_price * qty)) over(order by sum(unit_price * qty) desc) as rolling_sum_sales_from_top,
       sum(1) over(order by sum(unit_price * qty) desc) as products_,
       sum(1) over() AS total_products

from products p 
Left join sales s  on p.product_id = s.product_id  -- Left join because there might be unsold products
GROUP by product_name
)

select *, 
       grand_total_sales * 0.8 as toal_sale_80_perc,
       total_products * 0.2 as total_prod_20_perc, 
       case when products_ = (total_products * 0.2) and (grand_total_sales * 0.8) <= rolling_sum_sales_from_top then 1 else 0 end as '80-20 rule'
from base

```

<ins>**Got sum of all products, with sum per product**</ins>

| product_name | sales | grand_total_sales | rolling_sum_sales_from_top | products_ | total_products | toal_sale_80_perc | total_prod_20_perc | _80_20_rule |
|--------------|------:|------------------:|---------------------------:|----------:|---------------:|------------------:|-------------------:|------------:|
| Headphones   | 12000 | 91080             | 73100                      | 4         | 20             | 72864             | 4                  | 1           |



------------------------------------------------------------------------------------------------------------------------------------------------------

**6.hhhhhh**

------------------------------------------------------------------------------------------------------------------------------------------------------
























