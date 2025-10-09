with cte1 as (
    select
        *,
        id - row_number() over(order by id) as grp
    from Stadium
    where people >= 100
),
cte2 as (
    select
        *,
        count(*) over(partition by grp) as grp_size
    from cte1
)
select
    id,
    visit_date,
    people
from cte2
where grp_size >= 3
order by visit_date