SELECT
    sale_date,
    MAX(CASE WHEN fruit = 'apples' THEN sold_num ELSE 0 END) - MAX(CASE WHEN fruit = 'oranges' THEN sold_num ELSE 0 END) AS diff
FROM Sales
GROUP BY sale_date
ORDER BY sale_date