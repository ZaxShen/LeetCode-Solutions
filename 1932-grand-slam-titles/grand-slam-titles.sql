WITH cte AS (
    SELECT Wimbledon AS grand_slam FROM Championships
    UNION ALL
    SELECT Fr_open AS grand_slam FROM Championships
    UNION ALL
    SELECT US_open AS grand_slam FROM Championships
    UNION ALL
    SELECT Au_open AS grand_slam FROM Championships
)
SELECT
    p.player_id,
    p.player_name,
    COUNT(grand_slam) AS grand_slams_count
FROM
    Players p
    JOIN cte c ON p.player_id = c.grand_slam
GROUP BY
    p.player_id,
    p.player_name