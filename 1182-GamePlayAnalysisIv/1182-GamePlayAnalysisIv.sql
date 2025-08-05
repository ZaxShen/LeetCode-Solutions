-- Last updated: 8/4/2025, 10:46:09 PM
with day1 as (
    select
        player_id,
        min(event_date) as event_date
    from Activity
    group by 1
)
select round(count(a.player_id) / count(d.player_id), 2) as fraction
from day1 as d
left join Activity a on d.player_id = a.player_id
and d.event_date + interval 1 day = a.event_date

    