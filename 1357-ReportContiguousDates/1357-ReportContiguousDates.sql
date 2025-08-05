-- Last updated: 8/4/2025, 10:45:42 PM
with cte(event_date, status) as
	(
    select fail_date, "failed"
    from Failed
    union
    select success_date, "succeeded"
    from Succeeded
    ),
cte1 as
	(
	select
		event_date,
        event_date - interval row_number() over(partition by status order by event_date) day as diff,
        status
	from cte
    where event_date between '2019-01-01' and '2019-12-31'
	)
select
	status as period_state,
    min(event_date) as start_date,
    max(event_date) as end_date
from cte1
group by 1, diff
order by 2;