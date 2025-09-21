SELECT
    COUNT(account_id) AS accounts_count
FROM
    Subscriptions
    JOIN Streams USING (account_id)
WHERE
    EXTRACT(YEAR FROM end_date) = 2021
    AND EXTRACT(YEAR FROM stream_date) != 2021