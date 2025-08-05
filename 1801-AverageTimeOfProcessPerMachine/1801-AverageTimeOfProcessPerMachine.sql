-- Last updated: 8/4/2025, 10:44:14 PM
# Write your MySQL query statement below
select a0.machine_id, round(avg(a1.timestamp - a0.timestamp), 3) as processing_time
from Activity a0
inner join Activity a1
    on a0.activity_type = 'start'
    and a1.activity_type = 'end'
    and a0.machine_id = a1.machine_id
    and a0.process_id = a1.process_id
group by 1