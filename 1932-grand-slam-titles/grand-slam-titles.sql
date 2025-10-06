with cte as (
    select Wimbledon as grand_slam from Championships
    union all
    select Fr_open as grand_slam from Championships
    union all
    select US_open as grand_slam from Championships
    union all
    select Au_open as grand_slam from Championships
)
select
    p.player_id,
    p.player_name,
    count(grand_slam) as grand_slams_count
from
    Players p
    join cte c on p.player_id = c.grand_slam
group by
    p.player_id,
    p.player_name
