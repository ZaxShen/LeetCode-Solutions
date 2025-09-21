select count(account_id) as accounts_count
from Subscriptions
where DATE('2021-01-01') <= end_date and end_date <= DATE('2021-12-31')
and account_id not in (select distinct account_id from Streams where extract(year from stream_date) = '2021')