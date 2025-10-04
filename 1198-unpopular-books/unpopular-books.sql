SELECT 
    b.book_id,
    b.name
FROM Books b
LEFT JOIN Orders o 
    ON b.book_id = o.book_id 
    AND o.dispatch_date <= '2019-06-23'
    AND o.dispatch_date >= '2019-06-23'::DATE - INTERVAL '1 year'
WHERE b.available_from < '2019-06-23'::DATE - INTERVAL '1 month'
GROUP BY b.book_id, b.name
HAVING COALESCE(SUM(o.quantity), 0) < 10
ORDER BY b.book_id