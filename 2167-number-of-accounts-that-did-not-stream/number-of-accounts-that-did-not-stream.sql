select count(account_id) as accounts_count
from Subscriptions su
where start_date < '2022-01-01'::DATE and end_date >= '2021-01-01'::DATE
    and not exists (
        select 1
        from Streams st
        where su.account_id = st.account_id
            and extract(year from st.stream_date) = 2021
    )