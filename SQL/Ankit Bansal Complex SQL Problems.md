# Ankit Bansal Complex SQL Playlist  
(link - https://youtube.com/playlist?list=PLBTZqjSKn0IeKBQDjLmzisazhqQy4iGkb&si=FvqEB_MTceoJ_8KF)


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


`with base as (
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
`
