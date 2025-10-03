with cte as (
    select
        num,
        lag(num, 1) over() as lag_1,
        lag(num, 2) over() as lag_2
    from logs
)
select distinct num as ConsecutiveNums
from cte
where num = lag_1 and num = lag_2