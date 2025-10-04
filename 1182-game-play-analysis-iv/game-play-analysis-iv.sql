with day1 as (
    select
        player_id,
        min(event_date) as day1,
        min(event_date) + 1 as day2
    from Activity
    group by player_id
)
select 
    round(count(a.player_id)::numeric / count(d.player_id), 2) as fraction
from day1 d
    left join Activity a on d.player_id = a.player_id
        and d.day2 = a.event_date