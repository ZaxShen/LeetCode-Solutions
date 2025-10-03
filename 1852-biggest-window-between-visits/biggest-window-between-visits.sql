WITH
    cte AS (
        SELECT
            *,
            COALESCE(
                LEAD(visit_date, 1) OVER (PARTITION BY user_id ORDER BY visit_date ASC),
                '2021-1-1'::DATE
            ) AS date_lead
        FROM UserVisits
    )
SELECT
    user_id,
    MAX(date_lead - visit_date) AS biggest_window
FROM cte
GROUP BY user_id
ORDER BY user_id