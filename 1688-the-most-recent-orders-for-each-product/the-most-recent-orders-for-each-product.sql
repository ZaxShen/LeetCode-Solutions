WITH cte AS (
    SELECT
        p.product_name,
        o.product_id,
        o.order_id,
        o.order_date,
        DENSE_RANK() OVER (PARTITION BY o.product_id ORDER BY o.order_date DESC) AS order_date_desc
    FROM
        Orders o
        JOIN Products p ON o.product_id = p.product_id
)
SELECT
    product_name,
    product_id,
    order_id,
    order_date
FROM cte
WHERE order_date_desc = 1
ORDER BY
    product_name,
    product_id,
    order_id