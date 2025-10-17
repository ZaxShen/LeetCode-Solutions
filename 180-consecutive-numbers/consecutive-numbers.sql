with cte as (

select
    num,
    lead(num, 1) over(order by id) as lag_1,
    lead(num, 2) over(order by id) as lag_2
from logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM cte
WHERE
    num = lag_1
    AND num = lag_2