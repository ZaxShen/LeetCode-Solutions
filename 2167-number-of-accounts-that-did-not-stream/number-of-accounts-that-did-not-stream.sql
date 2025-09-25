select count(*) as accounts_count
from Subscriptions su
left join Streams st using(account_id)
where extract(year from su.end_date) = 2021
    and extract(year from st.stream_date) != 2021