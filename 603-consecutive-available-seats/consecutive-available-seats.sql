with grps as (
    select
        seat_id,
        seat_id - row_number() over(order by seat_id) as grp
    from Cinema
    where free = 1
),
cte as (
    select
        seat_id,
        count(*) over(partition by grp) as grp_size
    from grps
)
select seat_id
from cte
where grp_size >= 2