-- Last updated: 8/4/2025, 10:46:03 PM
with cte as
	(
    select user_id, min(activity_date) as first_login
    from Traffic
    where activity = 'login'
    group by 1
    )
select
    first_login as login_date,
    count(user_id) as user_count
from cte
where datediff('2019-06-30', first_login) <= 90
group by 1
order by 1;