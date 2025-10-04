with cte as (
    select
        player_id,
        device_id,
        rank() over(partition by player_id order by event_date) as event_date_asc
    from Activity
)

select
    player_id, 
    device_id
from cte
where event_date_asc = 1
