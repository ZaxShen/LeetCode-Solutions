-- Last updated: 8/4/2025, 10:45:26 PM
# Write your MySQL query statement below
select EmployeeUNI.unique_id, Employees.name
from Employees
left join EmployeeUNI
    on Employees.id = EmployeeUNI.id