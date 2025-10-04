WITH
    cte AS (
        SELECT
            s.user_id,
            s.product_id,
            DENSE_RANK() OVER (PARTITION BY s.user_id ORDER BY SUM(s.quantity * p.price) DESC) AS amount_desc
        FROM
            Sales s
            JOIN Product p ON s.product_id = p.product_id
        GROUP BY
            s.user_id,
            s.product_id
    )
SELECT
    user_id,
    product_id
FROM cte
WHERE amount_desc = 1