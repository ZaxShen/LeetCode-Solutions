-- Last updated: 8/4/2025, 10:45:53 PM
/*Select the product price at a given date

- Products PK: (product_id, change_date)

- SOLUTION: window function, UNION ALL
 */
WITH
    cte AS (
        SELECT
            product_id,
            MAX(change_date) AS change_date
        FROM
            Products
        WHERE
            change_date <= '2019-08-16'
        GROUP BY
            product_id
    )
SELECT
    cte.product_id,
    new_price AS price
FROM
    cte
    LEFT JOIN Products USING (product_id, change_date)
UNION ALL
SELECT DISTINCT
    product_id,
    10
FROM
    Products
WHERE
    product_id NOT IN (
        SELECT
            product_id
        FROM
            cte
    );
