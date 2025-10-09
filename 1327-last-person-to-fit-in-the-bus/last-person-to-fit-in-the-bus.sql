with cte as (
    select
        person_name,
        turn,
        sum(weight) over(order by turn) as acc_weight
    from Queue
)
select person_name
from cte
where acc_weight <= 1000
order by turn desc
limit 1