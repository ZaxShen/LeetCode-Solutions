WITH
    cte AS (
        SELECT
            o.customer_id,
            c.name,
            TO_CHAR(o.order_date, 'YYYY-MM') AS order_month,
            SUM(o.quantity * p.price) AS total
        FROM
            Orders o
            JOIN customers c USING (customer_id)
            JOIN product p USING (product_id)
        WHERE o.order_date BETWEEN '2020-06-01'::DATE AND '2020-07-31'::DATE
        GROUP BY
            o.customer_id,
            c.name,
            TO_CHAR(o.order_date, 'YYYY-MM')
    )
SELECT
    customer_id,
    name
FROM cte
GROUP BY
    customer_id,
    name
HAVING
    COUNT(*) = 2
    AND MIN(total) >= 100