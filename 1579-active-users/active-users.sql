WITH
    cte AS (
        SELECT
            id,
            login_date - INTERVAL '1 day' * ROW_NUMBER() OVER (
                PARTITION BY id ORDER BY login_date
            ) AS grp
        FROM (SELECT DISTINCT id, login_date FROM Logins)
    )
SELECT DISTINCT
    cte.id,
    a.name
FROM
    cte
    JOIN Accounts a ON cte.id = a.id
GROUP BY
    cte.id,
    a.name,
    grp
HAVING COUNT(grp) >= 5
ORDER BY cte.id