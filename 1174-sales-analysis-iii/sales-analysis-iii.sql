SELECT DISTINCT
    s.product_id,
    p.product_name
FROM Sales s
JOIN Product p ON s.product_id = p.product_id
WHERE NOT EXISTS (
    SELECT 1 
    FROM Sales s2 
    WHERE s2.product_id = s.product_id
      AND (s2.sale_date < '2019-01-01' OR s2.sale_date >= '2019-04-01')
)