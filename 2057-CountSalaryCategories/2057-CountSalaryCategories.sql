-- Last updated: 8/4/2025, 10:43:53 PM
WITH
    cte AS (
        SELECT
            account_id,
            income,
            CASE
                WHEN income < 20000 THEN 'Low Salary'
                WHEN income > 50000 THEN 'High Salary'
                ELSE 'Average Salary'
            END AS Category
        FROM
            Accounts
    ),
    categories (category) AS (
        SELECT
            'Low Salary'
        UNION
        SELECT
            'Average Salary'
        UNION
        SELECT
            'High Salary'
    )
SELECT
    c.category,
    IFNULL (COUNT(cte.Category), 0) AS accounts_count
FROM
    categories c
    LEFT JOIN cte USING (category)
GROUP BY
    1