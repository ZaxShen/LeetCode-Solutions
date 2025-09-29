with cte as (
    select
        person_name,
        turn,
        sum(weight) over(order by turn asc) as total_weight
    from Queue
)
select person_name
from cte
where total_weight <= 1000
order by turn desc
limit 1