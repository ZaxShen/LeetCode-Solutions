WITH all_credits AS (
    -- Initial credits
    SELECT user_id, credit FROM Users
    
    UNION ALL
    
    -- Money paid (negative)
    SELECT paid_by, -amount FROM Transactions
    
    UNION ALL
    
    -- Money received (positive)
    SELECT paid_to, amount FROM Transactions
)
SELECT
    u.user_id,
    u.user_name,
    SUM(ac.credit) AS credit,
    CASE
        WHEN SUM(ac.credit) < 0 THEN 'Yes'
        ELSE 'No'
    END AS credit_limit_breached
FROM
    Users u
    LEFT JOIN all_credits ac ON u.user_id = ac.user_id
GROUP BY
    u.user_id, u.user_name
ORDER BY
    u.user_id;