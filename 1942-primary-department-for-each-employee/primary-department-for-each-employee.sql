with cte as (
    select
        employee_id,
        department_id
    from Employee
    where primary_flag = 'Y'
)
select * from cte
union
select employee_id, department_id
from Employee
where employee_id not in (select employee_id from cte)
order by employee_id