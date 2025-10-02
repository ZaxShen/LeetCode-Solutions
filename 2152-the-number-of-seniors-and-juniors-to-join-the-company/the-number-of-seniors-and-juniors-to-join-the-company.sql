with acc_salary as (
    select
        employee_id,
        experience,
        salary,
        sum(salary) over(partition by experience order by salary, employee_id) as acc_salary
    from Candidates
    group by employee_id, experience, salary
), hired_seniors as (
    select
        experience,
        coalesce(acc_salary, 0) as acc_salary
    from acc_salary
    where experience = 'Senior'
        and acc_salary <= 70000
)
select
    'Senior' AS experience,
    count(*) as accepted_candidates
from hired_seniors
union all
select
    'Junior' as experience,
    count(*) as accepted_candidates
from acc_salary
where
    experience = 'Junior'
    and acc_salary <= 70000 - (
        select coalesce(max(acc_salary), 0)
        from hired_seniors
    )
