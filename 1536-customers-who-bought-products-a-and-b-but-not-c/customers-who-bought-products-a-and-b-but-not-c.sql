select
    c.customer_id,
    c.customer_name
from
    Customers c
    join Orders o on c.customer_id = o.customer_id
group by
    c.customer_id,
    c.customer_name
having
    sum((o.product_name = 'A')::INT) > 0
    and sum((o.product_name = 'B')::INT) > 0
    and sum((o.product_name = 'C')::INT) = 0
order by customer_id