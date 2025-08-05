-- Last updated: 8/4/2025, 10:44:24 PM
# Write your MySQL query statement below

WITH CTE AS
	(
    SELECT
		p.product_name, p.product_id,
        o.order_id, o.order_date,
        DENSE_RANK() OVER(PARTITION BY p.product_id ORDER BY order_date DESC) AS order_date_rank
	FROM Products p
    INNER JOIN Orders o ON p.product_id = o.product_id
    )
SELECT product_name, product_id, order_id, order_date
FROM CTE
WHERE order_date_rank = 1
ORDER BY product_name ASC, order_id ASC;