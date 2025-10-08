WITH cte AS (
    SELECT
        o.customer_id,
        -- DATE_TRUNC('month', o.order_date) AS year_month,
        SUM(p.price * o.quantity) AS amount
    FROM
        Orders o
        JOIN Product p ON o.product_id = p.product_id
    WHERE o.order_date BETWEEN '2020-06-01'::DATE AND '2020-07-31'::DATE
    GROUP BY
        customer_id,
        DATE_TRUNC('month', o.order_date)
)
SELECT
    cte.customer_id,
    c.name
FROM
    cte
    JOIN customers c ON cte.customer_id = c.customer_id
WHERE cte.amount >= 100
GROUP BY
    cte.customer_id,
    c.name
HAVING COUNT(*) = 2