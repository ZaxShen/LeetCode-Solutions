select
    count(*) as accounts_count
from Subscriptions su
where start_date < '2022-01-01'
    and end_date >= '2021-01-01'
    and not exists (
        select account_id
        from Streams st
        where extract(year from stream_date) = 2021
            and su.account_id = st.account_id
    )