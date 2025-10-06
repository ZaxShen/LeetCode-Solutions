with events(event_date, state) as (
    select fail_date, 'failed' from Failed
    union
    select success_date, 'succeeded' from Succeeded
), grps as (
    select
        state,
        event_date,
        event_date - interval '1 day' * row_number() over(partition by state order by event_date) as grp
    from events
    where event_date between '2019-01-01'::Date and '2019-12-31'::date
)
select
    state as period_state,
    min(event_date) as start_date,
    max(event_date) as end_date
from grps
group by period_state, grp
order by start_date