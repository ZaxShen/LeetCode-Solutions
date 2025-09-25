SELECT
    COUNT(distinct su.account_id) AS accounts_count
FROM
    subscriptions su
    LEFT JOIN streams st ON su.account_id = st.account_id 
WHERE
    -- ✅: Active subscription during 2021
    (su.start_date <= '2021-12-31' AND su.end_date >= '2021-01-01')
    -- ✅: No 2021 streams or no streams across all years
    -- ❌: May contains streams other than 2021 & 2021 streams, above session_id = 20 will be contained
    AND (EXTRACT(YEAR FROM st.stream_date) != 2021 OR st.stream_date IS NULL)