-- Last updated: 8/4/2025, 10:43:45 PM
# Write your MySQL query statement below
with cte as
	(
    select
		employee_id,
        experience,
        # salary,
        sum(salary) over(partition by experience order by salary, employee_id asc) as total_salary
	from Candidates
    ),
max_senior_salary as
	(
    select ifnull(max(total_salary), 0) as max_senior_salary
    from cte
    where experience = 'Senior' and total_salary <= 70000
    )
select 
	'Senior' as experience, 
    count(*) as accepted_candidates
from cte
where experience = 'Senior' and total_salary <= 70000
union all
select 
	'Junior' as experience, 
    count(*) as accepted_candidates
from cte
where experience = 'Junior' and total_salary <= 70000 - (select max_senior_salary from max_senior_salary);