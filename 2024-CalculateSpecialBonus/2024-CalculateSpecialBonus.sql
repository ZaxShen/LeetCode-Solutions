-- Last updated: 8/4/2025, 10:43:55 PM
select
    employee_id,
    if (employee_id % 2 = 1 and name not regexp "^M", salary, 0) as bonus
from Employees
order by 1;