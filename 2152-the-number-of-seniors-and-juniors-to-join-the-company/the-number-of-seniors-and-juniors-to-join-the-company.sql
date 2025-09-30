with cte as (
    select
        *,
        sum(salary) over(partition by experience order by salary asc, employee_id asc) as total_salary
    from Candidates
), 
max_senior_salary as (
    select coalesce(total_salary, 0) as total_salary
    from cte
    where experience = 'Senior' 
        and total_salary <= 70000
)
select
    'Senior' as experience,
    count(*) as accepted_candidates
from max_senior_salary
union all
select
    'Junior' as experience,
    count(*) as accepted_candidates
from cte
where experience = 'Junior'
    and total_salary <= 70000 - (select coalesce(max(total_salary), 0) from max_senior_salary)