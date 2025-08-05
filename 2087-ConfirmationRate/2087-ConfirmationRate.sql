-- Last updated: 8/4/2025, 10:43:52 PM
# Write your MySQL query statement below
select s.user_id, ifnull(round(sum(if(action = 'confirmed', 1, 0)) / count(action), 2), 0) as confirmation_rate
from Signups s
left join Confirmations c
    on s.user_id = c.user_id
group by 1