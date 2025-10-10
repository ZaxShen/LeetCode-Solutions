WITH day1 AS (
    SELECT
        player_id,
        MIN(event_date) AS day1,
        MIN(event_date) + 1 AS day2
    FROM Activity
    GROUP BY player_id
)
SELECT
    ROUND(COUNT(a.player_id)::NUMERIC / COUNT(d.player_id), 2) AS fraction
FROM
    day1 d
    LEFT JOIN Activity a ON d.player_id = a.player_id
    AND d.day2 = a.event_date