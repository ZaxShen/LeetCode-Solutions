with cte as (
    select
        player_id,
        min(event_date) as first_login
    from Activity
    group by player_id
)
select round(count(*)::NUMERIC / (select count(*) from cte), 2) as fraction
from
    cte c
    join Activity a on c.player_id = a.player_id
        and c.first_login + interval '1 day' = a.event_date
    