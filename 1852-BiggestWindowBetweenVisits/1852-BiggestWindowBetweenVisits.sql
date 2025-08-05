-- Last updated: 8/4/2025, 10:44:08 PM
# Write your MySQL query statement below
with cte as
	(
	select
		user_id,
		visit_date,
		lead(visit_date) over(partition by user_id order by visit_date) as date_lead
	from UserVisits
    )
select 
	user_id, 
    max(datediff(ifnull(date_lead, '2021-1-1'), visit_date)) as biggest_window
from cte
group by user_id;