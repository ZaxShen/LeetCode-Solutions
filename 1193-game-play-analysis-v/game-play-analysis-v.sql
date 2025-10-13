with cte as (
    select
        player_id,
        min(event_date) as install_dt
    from Activity
    group by player_id
)
select
    c.install_dt,
    count(c.player_id) as installs,
    round(count(a.player_id)::NUMERIC / count(c.player_id), 2) as Day1_retention
from
    cte c
    left join Activity a on c.install_dt + 1 = a.event_date
        and c.player_id = a.player_id
group by c.install_dt