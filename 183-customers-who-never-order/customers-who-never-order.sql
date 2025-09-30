select c."name" as "Customers"
from Customers c
where not exists (
    select distinct customerId
    from Orders o
    where c.id = o.customerId
)