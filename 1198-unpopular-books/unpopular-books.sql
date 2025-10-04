SELECT 
    b.book_id,
    b.name
FROM Books b
LEFT JOIN Orders o 
    ON b.book_id = o.book_id 
    AND o.dispatch_date BETWEEN '2018-06-23'::DATE AND '2019-06-23'::DATE
WHERE b.available_from < '2019-06-23'::DATE - INTERVAL '1 month'
GROUP BY b.book_id, b.name
HAVING COALESCE(SUM(o.quantity), 0) < 10
ORDER BY b.book_id;