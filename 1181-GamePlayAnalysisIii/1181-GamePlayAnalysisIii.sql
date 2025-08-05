-- Last updated: 8/4/2025, 10:46:10 PM
select player_id, event_date, sum(games_played) over(partition by player_id order by event_date asc) as games_played_so_far
from Activity