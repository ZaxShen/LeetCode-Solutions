select
    e.name as Employee
from Employee e
join Employee m on e.managerId = m.id
where e.Salary > m.Salary