-- Last updated: 8/4/2025, 10:43:57 PM
# Write your MySQL query statement below
select
    user_id,
    max(time_stamp) as last_stamp
from Logins
where year(time_stamp) = 2020
group by 1;