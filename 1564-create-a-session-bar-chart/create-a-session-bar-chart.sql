WITH bins AS (
    SELECT '[0-5>' AS bin, 1 AS bin_order
    UNION ALL SELECT '[5-10>', 2
    UNION ALL SELECT '[10-15>', 3
    UNION ALL SELECT '15 or more', 4
),
categorized AS (
    SELECT 
        CASE 
            WHEN duration / 60 < 5 THEN '[0-5>'
            WHEN duration / 60 < 10 THEN '[5-10>'
            WHEN duration / 60 < 15 THEN '[10-15>'
            ELSE '15 or more'
        END AS bin
    FROM Sessions
)
SELECT 
    b.bin,
    COALESCE(COUNT(c.bin), 0) AS total
FROM bins b
LEFT JOIN categorized c ON b.bin = c.bin
GROUP BY b.bin, b.bin_order
ORDER BY b.bin_order