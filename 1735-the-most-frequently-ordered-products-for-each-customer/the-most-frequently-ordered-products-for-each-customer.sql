WITH cte AS (
    SELECT
        o.customer_id,
        o.product_id,
        p.product_name,
        DENSE_RANK() OVER (PARTITION BY o.customer_id ORDER BY COUNT(o.order_id) DESC) AS order_count_desc
    FROM
        Orders o
        JOIN Products p ON o.product_id = p.product_id
    GROUP BY
        o.customer_id,
        o.product_id,
        p.product_name
)
SELECT
    customer_id,
    product_id,
    product_name
FROM cte
WHERE order_count_desc = 1
ORDER BY
    product_name,
    product_id,
    customer_id