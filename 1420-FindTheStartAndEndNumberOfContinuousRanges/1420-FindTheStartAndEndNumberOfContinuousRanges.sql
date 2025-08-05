-- Last updated: 8/4/2025, 10:45:35 PM
with cte as
    (
    select
        log_id,
        log_id - row_number() over() as diff
    from Logs
    )
select
    min(log_id) as start_id,
    max(log_id) as end_id
from cte
group by diff;