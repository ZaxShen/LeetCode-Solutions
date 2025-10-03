with cte as (
    select
        *,
        coalesce(
            lead(visit_date, 1) over(partition by user_id order by visit_date asc), 
        '2021-1-1'::DATE) date_lead
    from UserVisits
)
select
    user_id,
    max(date_lead - visit_date) as biggest_window
from cte
group by user_id
order by user_id