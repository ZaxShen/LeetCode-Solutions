-- Last updated: 8/4/2025, 10:46:02 PM
# Write your MySQL query statement below
with cte as
    (
    select event_type, avg(occurences) as avg_activity
    from Events
    group by 1
    )
select business_id
from Events
inner join cte using(event_type)
where occurences > avg_activity
group by 1
having count(*) > 1;
