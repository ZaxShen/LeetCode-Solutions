with day1 as (
    select
        player_id,
        min(event_date) as day1,
        min(event_date) + 1 as day2
    from Activity
    group by player_id
)
select
    d.day1 as install_dt,
    count(d.player_id) as installs,
    round(count(a.player_id)::numeric / count(d.player_id), 2) as Day1_retention
from day1 d
    left join Activity a on d.player_id = a.player_id
        and d.day2 = a.event_date
group by d.day1
order by d.day1