-- Last updated: 8/4/2025, 10:44:26 PM
# Write your MySQL query statement below

WITH CTE AS
	(
	SELECT name AS customer_name, c.customer_id, order_id, order_date,
		DENSE_RANK() OVER (PARTITION BY c.customer_id ORDER BY order_date DESC) AS ranking
	FROM Customers c
	LEFT JOIN Orders o ON c.customer_id = o.customer_id
    )
SELECT customer_name, customer_id, order_id, order_date
FROM CTE
WHERE ranking IN (1, 2, 3) AND order_date IS NOT NULL
ORDER BY customer_name ASC, customer_id ASC, order_date DESC;