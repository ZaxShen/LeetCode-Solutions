with recursive cte as (
    select 1 as employee_id
    union
    select e.employee_id
    from Employees e
    join cte on e.manager_id = cte.employee_id
)
select employee_id
from cte
where employee_id != 1