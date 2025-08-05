-- Last updated: 8/4/2025, 10:45:27 PM
with cte as
	(
	select
		activity,
		rank() over(order by count(id) asc) as ar_activity,
		rank() over(order by count(id) desc) dr_activity
	from Friends
	group by activity
    )
select activity
from cte
where ar_activity != 1
	and dr_activity != 1;