with cte as (
    select
        user_id,
        min(activity_date) as first_login
    from Traffic
    where activity = 'login'
    group by user_id
)
select
    first_login as login_date,
    count(*) as user_count
from cte
where '2019-06-30'::DATE - first_login <= 90
group by login_date