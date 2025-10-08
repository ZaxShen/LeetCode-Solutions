with grps as (
    select
        *,
        id - row_number() over(order by visit_date) as grp
    from Stadium
    where people >= 100
),
date_count as (
    select
        *,
        count(id) over(partition by grp) as grp_size
    from grps
)
select
    id,
    visit_date,
    people
from date_count
where grp_size >= 3
order by visit_date