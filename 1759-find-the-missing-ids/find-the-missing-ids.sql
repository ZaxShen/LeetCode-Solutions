WITH RECURSIVE cte AS (
    SELECT 1 AS ids
    UNION
    SELECT ids + 1
    FROM cte
    WHERE ids < (SELECT MAX(customer_id) FROM Customers)
)
SELECT cte.ids
FROM
    cte
    LEFT JOIN Customers c on cte.ids = c.customer_id
WHERE c.customer_id IS NULL
ORDER BY ids