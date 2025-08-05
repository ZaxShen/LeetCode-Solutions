-- Last updated: 8/4/2025, 10:46:21 PM
-- O(nlogn), O(n)
SELECT
    customer_id
FROM
    Customer
GROUP BY
    customer_id
HAVING
    COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)