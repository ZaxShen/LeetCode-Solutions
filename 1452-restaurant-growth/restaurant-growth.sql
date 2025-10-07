WITH cte AS (
	SELECT
		visited_on,
		SUM(amount) AS daily_total,
		SUM(SUM(amount)) OVER (
			ORDER BY visited_on 
			ROWS BETWEEN 6 preceding AND CURRENT ROW
		) AS rolling_sum_7d,
		AVG(SUM(amount)) OVER (
			ORDER BY visited_on 
			ROWS BETWEEN 6 preceding AND CURRENT ROW 
		) AS rolling_avg_7d
	FROM Customer
	GROUP BY visited_on
)
SELECT
    visited_on,
    rolling_sum_7d AS amount,
    ROUND(rolling_avg_7d, 2) AS average_amount
FROM cte
OFFSET 6