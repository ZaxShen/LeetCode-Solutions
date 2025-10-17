WITH cte AS (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY 1) AS lag_1,
        LAG(num, 2) OVER (ORDER BY 1) AS lag_2
    FROM
        logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM cte
WHERE
    num = lag_1
    AND num = lag_2