-- Last updated: 8/4/2025, 10:45:55 PM
SELECT
    u.user_id AS buyer_id,
    join_date,
    COUNT(order_id) AS orders_in_2019
FROM
    Users u
    LEFT JOIN Orders o ON u.user_id = o.buyer_id
    AND YEAR (order_date) = 2019
GROUP BY
    1,
    2