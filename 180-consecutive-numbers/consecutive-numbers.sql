with cte as (
    select
        *,
        id - rank() over (partition by num order by id) as grp
    from Logs
)
select distinct num as ConsecutiveNums
from cte
group by num, grp
    having count(*) >= 3