WITH cte AS (
    SELECT 
        id,
        num,
        id - DENSE_RANK() OVER(PARTITION BY num ORDER BY id ASC) AS diff
    FROM Logs
)
-- select * from cte;
SELECT DISTINCT num AS ConsecutiveNums
FROM cte
GROUP BY num, diff
HAVING COUNT(*) >= 3;