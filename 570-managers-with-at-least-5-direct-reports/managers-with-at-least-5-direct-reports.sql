with managers as (
select managerId
from employee
group by managerId
having count(*) >= 5
)
select name
from employee e
join managers m on e.id = m.managerId