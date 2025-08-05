-- Last updated: 8/4/2025, 10:45:19 PM
# Write your MySQL query statement below

WITH CTE AS
	(
	SELECT
		user_id,
        SUM(distance) AS travelled_distance
	FROM
		Rides
	GROUP BY
		user_id
	)
SELECT
	name,
    IFNULL(travelled_distance, 0) AS travelled_distance
FROM
	Users u
LEFT JOIN
	CTE c ON u.id = c.user_id
ORDER BY
	travelled_distance DESC, name ASC
;