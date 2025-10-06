SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) FILTER (
	    WHERE EXTRACT(YEAR FROM o.order_date) = 2019
	) AS orders_in_2019
FROM
    Users u
    LEFT JOIN Orders o ON u.user_id = o.buyer_id
GROUP BY
    u.user_id,
    u.join_date