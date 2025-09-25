SELECT
    COUNT(su.account_id) AS accounts_count
FROM
    subscriptions su
    LEFT JOIN streams st ON su.account_id = st.account_id 
        AND EXTRACT(YEAR FROM st.stream_date) = 2021
WHERE
    -- Subscription was active during 2021
    (su.start_date <= '2021-12-31' AND su.end_date >= '2021-01-01')
    -- No streams in 2021
    AND st.account_id IS NULL;