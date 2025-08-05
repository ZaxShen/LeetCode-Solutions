-- Last updated: 8/4/2025, 10:45:58 PM
# Write your MySQL query statement below
select activity_date as `day`, count(distinct user_id) as active_users
from Activity
where activity_date between ('2019-07-27' - interval 29 day) and '2019-07-27'
group by 1
order by 1 asc