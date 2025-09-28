-- count employee_id by project_id
-- get the max

with project_emp_rank as (
    select
        project_id,
        dense_rank() over(order by count(*) desc) as project_desc
    from Project
    group by project_id
)
select project_id
from project_emp_rank
where project_desc = 1
