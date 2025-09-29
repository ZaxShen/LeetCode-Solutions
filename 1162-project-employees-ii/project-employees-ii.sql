with cte as (
    select
        p.project_id,
        dense_rank() over(order by count(*) desc) as emp_count_desc
    from Project p
        join Employee e using (employee_id)
    group by p.project_id
)
select project_id
from cte
where emp_count_desc = 1