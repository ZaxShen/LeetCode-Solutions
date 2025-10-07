select distinct s.ids
from
    Customers c1
    cross join generate_series(1, (select max(customer_id) from Customers)) as s(ids)
    left join Customers c2 on s.ids = c2.customer_id
where c2.customer_id IS NULL
order by ids