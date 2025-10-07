WITH cte AS (
    SELECT user_id, credit FROM Users
    UNION ALL
    SELECT paid_by, -amount FROM Transactions
    UNION ALL
    SELECT paid_to, amount FROM Transactions
)
SELECT
    u.user_id,
    u.user_name,
    SUM(c.credit) AS credit,
    CASE
        WHEN SUM(c.credit) < 0 THEN 'Yes'
        ELSE 'No'
    END AS credit_limit_breached
FROM
    Users u
    JOIN cte c ON u.user_id = c.user_id
GROUP BY
    u.user_id,
    u.user_name
ORDER BY u.user_id