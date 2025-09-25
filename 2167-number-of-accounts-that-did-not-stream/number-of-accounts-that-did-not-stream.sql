select count(*) as accounts_count
from Subscriptions
where extract(year from end_date) = 2021
    and account_id not in (
        select distinct account_id
        from Streams
        where extract(year from stream_date) = 2021
    )