select
    id,
    name
from Students
where department_id not in (select distinct id from Departments)