-- Last updated: 8/4/2025, 10:43:47 PM
# Write your MySQL query statement below
select employee_id
from Employees
where salary < 30000
and manager_id not in (select employee_id from Employees)
order by employee_id asc