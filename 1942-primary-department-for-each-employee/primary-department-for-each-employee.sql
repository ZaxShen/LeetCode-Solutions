select distinct on (employee_id)
    employee_id,
    department_id
from Employee
order by employee_id, primary_flag desc