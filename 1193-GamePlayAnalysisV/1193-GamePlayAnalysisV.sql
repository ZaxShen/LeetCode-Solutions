-- Last updated: 8/4/2025, 10:46:07 PM
with day1 as (
    select
        player_id,
        min(event_date) as event_date
    from Activity
    group by player_id
)
select
    day1.event_date as install_dt,
    count(day1.player_id) as installs,
    round(count(day2.player_id) / count(day1.player_id), 2) as Day1_retention
from day1
    left join Activity day2
    on day2.player_id = day1.player_id
    and day2.event_date = day1.event_date + interval 1 day
group by day1.event_date