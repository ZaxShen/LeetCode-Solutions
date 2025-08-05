-- Last updated: 8/4/2025, 10:44:06 PM
# Write your MySQL query statement below
select
    user_id,
    count(follower_id) as followers_count
from Followers
group by 1
order by 1 asc