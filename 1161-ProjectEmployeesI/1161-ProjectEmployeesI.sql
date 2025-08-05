-- Last updated: 8/4/2025, 10:46:16 PM
# Write your MySQL query statement below
select project_id, round(avg(experience_years), 2) as average_years
from Project p
inner join Employee e
    using(employee_id)
group by 1