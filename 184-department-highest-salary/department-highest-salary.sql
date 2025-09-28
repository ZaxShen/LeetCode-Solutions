with department_salary_rank as (
    select
        id,
        name,
        salary,
        dense_rank() over(partition by departmentId order by salary desc) salary_desc,
        departmentId
    from Employee
)
select
    d.name as Department,
    dsr.name as Employee,
    dsr.salary as Salary
from department_salary_rank dsr
join Department d on dsr.departmentId = d.id
where salary_desc = 1