-- Last updated: 8/4/2025, 10:45:38 PM
/* Select the employees that report to the head.

- Employees PK: employee_id

- SOLUTION: WITH RECURSIVE; UNION ALL
*/
with recursive
cte(employee_id, manager_id) as
	(
	select employee_id, cast(manager_id as char(30))
	from Employees
	where employee_id = 1
	union all
	select e.employee_id, concat(e.employee_id, '-->', c.manager_id)
	from Employees e
    inner join cte c on e.manager_id = c.employee_id
	where e.employee_id != 1
	)
select employee_id
from cte
where employee_id != 1;