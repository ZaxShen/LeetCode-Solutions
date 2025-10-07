with grps as (
    select
        *,
        seat_id - row_number() over(partition by free order by seat_id) as grp
    from Cinema
    where free = 1
),
seat_counts as (
    select
        seat_id,
        count(seat_id) over(partition by grp) as group_size
    from grps
)
select seat_id
from seat_counts
where group_size >= 2
order by seat_id