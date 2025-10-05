select
    activity_date as day,
    count(distinct user_id) as active_users
from Activity
where activity_date between '2019-06-28'::date and '2019-07-27'::Date
group by activity_date
order by day