-- Last updated: 8/4/2025, 10:45:47 PM
# Write your MySQL query statement below
with cte as (
    select *,
    sum(weight) over(order by turn asc) as total_weight
    from Queue
)
select person_name
from cte
where total_weight <= 1000
order by total_weight desc
limit 1;