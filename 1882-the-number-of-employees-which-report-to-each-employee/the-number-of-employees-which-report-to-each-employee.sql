select
    m.employee_id,
    m."name",
    count(e.employee_id) as reports_count,
    round(avg(e.age), 0) as average_age
from
    Employees m
    join Employees e on m.employee_id = e.reports_to
group by m.employee_id, m."name"
order by employee_id