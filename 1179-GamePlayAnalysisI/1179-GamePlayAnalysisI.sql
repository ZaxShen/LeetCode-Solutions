-- Last updated: 8/4/2025, 10:46:11 PM
select player_id, min(event_date) as first_login
from Activity
group by 1;