-- Last updated: 8/4/2025, 10:44:02 PM
# Write your MySQL query statement below
select employee_id, department_id
from Employee
where primary_flag = 'Y'
union
select employee_id, department_id
from Employee
group by 1
having count(*) = 1
order by 1 asc