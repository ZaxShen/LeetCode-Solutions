with cte as (
    select
        activity,
        dense_rank() over(order by count(*) asc) participants_asc,
        dense_rank() over(order by count(*) desc) participants_desc
    from Friends
    group by activity
)
select activity
from cte
where participants_asc != 1 and participants_desc != 1