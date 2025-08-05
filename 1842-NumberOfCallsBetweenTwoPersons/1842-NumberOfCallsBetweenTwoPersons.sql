-- Last updated: 8/4/2025, 10:44:09 PM
with cte as
    (
    select from_id as person1, to_id as person2, duration
    from Calls
    union all
    select to_id as person1, from_id as person2, duration
    from Calls
    )
select
    person1,
    person2,
    count(*) as call_count,
    sum(duration) as total_duration
from cte
group by 1, 2
having person2 < person1;