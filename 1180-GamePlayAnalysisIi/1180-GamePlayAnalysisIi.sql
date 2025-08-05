-- Last updated: 8/4/2025, 10:46:10 PM
select distinct
    player_id,
    first_value(device_id) over(partition by player_id order by event_date) as device_id
from Activity