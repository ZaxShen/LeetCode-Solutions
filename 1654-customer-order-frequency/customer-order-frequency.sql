WITH
    customer_spend AS (
        SELECT
            o.customer_id,
            c.name,
            DATE_TRUNC('month', o.order_date) AS month_year,
            SUM(p.price * o.quantity) AS monthly_spend
        FROM
            orders o
            JOIN customers c USING (customer_id)
            JOIN product p USING (product_id)
        WHERE
            o.order_date >= '2020-06-01'
            AND o.order_date < '2020-08-01'
        GROUP BY
            o.customer_id,
            c.name,
            DATE_TRUNC('month', o.order_date)
        HAVING
            SUM(p.price * o.quantity) >= 100
    )
SELECT
    customer_id,
    NAME
FROM
    customer_spend
GROUP BY
    customer_id,
    NAME
HAVING
    COUNT(*) = 2