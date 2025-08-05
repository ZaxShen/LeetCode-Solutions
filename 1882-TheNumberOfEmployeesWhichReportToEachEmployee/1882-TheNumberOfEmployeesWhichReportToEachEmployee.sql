-- Last updated: 8/4/2025, 10:44:05 PM
# Write your MySQL query statement below
select
    e1.reports_to as employee_id,
    e2.name,
    count(e1.reports_to) as reports_count,
    round(avg(e1.age), 0) as average_age
from Employees e1
inner join Employees e2
    on e1.reports_to = e2.employee_id
where e1.reports_to is not null
group by 1, 2
order by 1 asc