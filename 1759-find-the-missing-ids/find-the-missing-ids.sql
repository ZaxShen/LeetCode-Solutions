SELECT s.ids
FROM 
    GENERATE_SERIES(1, (SELECT MAX(customer_id) FROM Customers)) AS s(ids)
    LEFT JOIN Customers c on s.ids = c.customer_id
WHERE c.customer_id IS NULL
ORDER BY ids