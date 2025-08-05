-- Last updated: 8/4/2025, 10:44:21 PM
# Write your MySQL query statement below

WITH CTE AS
    (
    SELECT
        customer_id,
        product_id,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY COUNT(order_id) DESC) as count_orders_rank
    FROM Orders
    GROUP BY customer_id, product_id
    )
SELECT
    CTE.customer_id, CTE.product_id,
    Products.product_name
FROM CTE
INNER JOIN Products ON CTE.product_id = Products.product_id
WHERE count_orders_rank = 1;