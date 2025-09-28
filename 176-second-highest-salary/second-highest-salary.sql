with salary_rank as (
    select
        salary,
        dense_rank() over(order by salary desc) as salary_desc
    from Employee
)
select max(salary) as SecondHighestSalary
from salary_rank
where salary_desc = 2