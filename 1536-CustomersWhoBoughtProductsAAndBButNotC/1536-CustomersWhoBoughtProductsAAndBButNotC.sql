-- Last updated: 8/4/2025, 10:45:21 PM
/*Customers Who Bought Products A and B but Not C
- Customers PK: customer_id
- Orders PK: order_id

- SOLUTION: subquery
*/
SELECT customer_id, customer_name
FROM Customers
WHERE customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'A')
	AND customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'B')
    AND customer_id NOT IN (SELECT customer_id FROM Orders WHERE product_name = 'C');