with cte1 as (
    select
        seat_id,
        seat_id - row_number() over(order by seat_id) as grp
    from Cinema
    where free = 1
),
cte2 as (
    select
        seat_id,
        grp,
        count(*) over(partition by grp) as grp_size
    from cte1
)
select seat_id
from cte2
where grp_size >= 2
order by seat_id asc