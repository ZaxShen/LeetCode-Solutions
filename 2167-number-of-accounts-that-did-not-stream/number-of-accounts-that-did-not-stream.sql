-- get subscription valid in 2021
-- get streams in 2021
select
    count(*) as accounts_count
from Subscriptions su
where su.start_date < '2022-01-01'
    and su.end_date >= '2021-01-01'
    and not exists (
        select 1
        from Streams st
        where su.account_id = st.account_id
            and extract(year from st.stream_date) = 2021
    )