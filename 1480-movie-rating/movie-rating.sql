(
SELECT name AS results
FROM
    MovieRating m
    INNER JOIN Users u USING (user_id)
GROUP BY m.user_id, u.name
ORDER BY
    COUNT(user_id) DESC,
    name
LIMIT 1
)
UNION ALL
(
SELECT m.title AS results
FROM
    MovieRating mr
    INNER JOIN Movies m USING (movie_id)
WHERE TO_CHAR(created_at, 'YYYY-MM') = '2020-02'
GROUP BY m.title
ORDER BY
    AVG(rating) DESC,
    title
LIMIT 1
)