-- Last updated: 8/5/2025, 12:19:00 AM
# Write your MySQL query statement below
with cte as
    (
    select
        company_id,
        case
            when max(salary) < 1000 then 0
            when max(salary) <= 10000 then .24
            else .49
        end as tax_rate
    from Salaries
    group by 1
    )
select
    company_id, employee_id, employee_name,
    round(salary * (1 - tax_rate), 0) as salary
from Salaries
left join cte using(company_id);