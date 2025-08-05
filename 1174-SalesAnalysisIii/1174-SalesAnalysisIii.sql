-- Last updated: 8/4/2025, 10:46:12 PM
WITH cte AS (
    SELECT
        product_id,
        MIN(sale_date) AS first_sale_date,
        MAX(sale_date) AS last_sale_date
    FROM
        Sales
    GROUP BY
        product_id
)
SELECT
    p.product_id,
    p.product_name
FROM
    Product p
    INNER JOIN cte ON p.product_id = cte.product_id
WHERE
    cte.first_sale_date >= '2019-01-01'
    AND cte.last_sale_date <= '2019-03-31';