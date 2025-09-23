select 
    count(*) as accounts_count
from subscriptions
left join streams using(account_id)
where extract(year from end_date) = 2021
    and extract(year from stream_date) != 2021