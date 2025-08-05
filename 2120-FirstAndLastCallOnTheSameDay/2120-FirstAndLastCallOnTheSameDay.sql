-- Last updated: 8/4/2025, 10:43:48 PM
# Write your MySQL query statement below
with cte as
	(
	select 
		caller_id as a, 
        recipient_id as b, 
        call_time
	from Calls
	union all
	select 
		recipient_id as a, 
        caller_id as b, 
        call_time
	from Calls
    ),
cte1 as
	(
	select
		a,
        b,
        date(call_time) as call_date,
		dense_rank() over(partition by a, date(call_time) order by call_time) as call_ar,
		dense_rank() over(partition by a, date(call_time) order by call_time desc) as call_dr
	from cte
	)
select distinct a as user_id
from cte1
where call_ar = 1 or call_dr = 1
group by 1, call_date
having count(distinct(b)) = 1;