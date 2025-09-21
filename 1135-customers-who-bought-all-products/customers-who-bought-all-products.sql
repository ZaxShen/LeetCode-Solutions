SELECT
    customer_id
FROM
    Product
    LEFT JOIN Customer USING (product_key)
GROUP BY
    customer_id
HAVING
    COUNT(DISTINCT Customer.product_key) = (
        SELECT
            COUNT(*)
        FROM
            Product
    )