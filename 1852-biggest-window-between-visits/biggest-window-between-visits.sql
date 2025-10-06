with cte as (
    select
        *,
        coalesce(
            lead(visit_date, 1) over(partition by user_id order by visit_date), 
        '2021-01-01'::DATE) as date_lead
    from UserVisits
)
select
    user_id,
    max(date_lead - visit_date) as biggest_window
from cte
group by user_id
order by user_id