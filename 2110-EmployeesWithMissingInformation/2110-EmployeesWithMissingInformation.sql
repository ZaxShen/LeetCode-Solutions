-- Last updated: 8/4/2025, 10:43:49 PM
# Write your MySQL query statement below
select employee_id
from Employees
where employee_id not in (select employee_id from Salaries)
union
select employee_id
from Salaries
where employee_id not in (select employee_id from Employees)
order by employee_id;