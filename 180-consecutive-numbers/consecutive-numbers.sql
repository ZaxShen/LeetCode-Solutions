with cte as (
    select
        num,
        id - row_number() over(partition by num order by id) as grp
    from Logs
)
select distinct num as ConsecutiveNums
from cte
group by num, grp
having count(num) >= 3