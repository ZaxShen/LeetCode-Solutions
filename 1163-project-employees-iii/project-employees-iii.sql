-- rank exp
-- select
with cte as (
    select
        project_id,
        p.employee_id,
        dense_rank() over(partition by p.project_id order by e.experience_years desc) as exp_desc
    from Project p
        join Employee e using(employee_id)
)
select project_id, employee_id
from cte
where exp_desc = 1
order by project_id asc, employee_id asc