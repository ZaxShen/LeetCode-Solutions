WITH
    cte AS (
        SELECT
            r1.user_id AS user1_id,
            r2.user_id AS user2_id,
            COUNT(*) AS common_followers,
            DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS common_followers_desc
        FROM
            Relations r1
            JOIN Relations r2 ON r1.follower_id = r2.follower_id
            AND r1.user_id < r2.user_id
        GROUP BY
            r1.user_id,
            r2.user_id
    )
SELECT
    user1_id,
    user2_id
FROM cte
WHERE common_followers_desc = 1