select
    count(account_id) as accounts_count
from Subscriptions su
where
    su.end_date >= '2021-01-01'
    and su.start_date < '2022-01-01'
    and not exists (
    select 1
    from Streams st
    where su.account_id = st.account_id
    and extract(year from st.stream_date) = 2021
)