-- Last updated: 8/4/2025, 10:45:33 PM
# Write your MySQL query statement below
select
    employee_id,
    count(*) over(partition by team_id) as team_size
from Employee;