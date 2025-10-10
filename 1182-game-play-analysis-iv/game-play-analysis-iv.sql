WITH cte AS (
    SELECT
        player_id,
        -- MIN(event_date) AS day1,
        MIN(event_date) + 1 AS day2
    FROM Activity
    GROUP BY player_id
)
SELECT
    ROUND(COUNT(a.player_id)::NUMERIC / COUNT(c.player_id), 2) AS fraction
FROM
    cte c
    LEFT JOIN Activity a ON c.player_id = a.player_id
    AND c.day2 = a.event_date