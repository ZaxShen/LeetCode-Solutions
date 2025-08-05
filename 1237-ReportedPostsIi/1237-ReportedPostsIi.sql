-- Last updated: 8/4/2025, 10:45:59 PM
# Write your MySQL query statement below
with cte as
	(
	select
		action_date, 
        count(distinct r.post_id) / count(distinct a.post_id) * 100 as daily_percent
	from Actions a
	left join Removals r on a.post_id = r.post_id
	where extra = 'spam'
	group by action_date
    )
select round(avg(daily_percent), 2) as average_daily_percent
from cte;