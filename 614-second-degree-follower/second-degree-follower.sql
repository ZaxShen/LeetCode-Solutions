SELECT
    followee AS follower,
    COUNT(*) AS num
FROM
    follow
WHERE
    followee IN (
        SELECT DISTINCT
            follower
        FROM
            follow
    )
GROUP BY
    followee
ORDER BY
    follower ASC