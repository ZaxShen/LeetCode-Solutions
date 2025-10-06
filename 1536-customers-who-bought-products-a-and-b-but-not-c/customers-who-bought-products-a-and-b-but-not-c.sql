select
    o.customer_id,
    c.customer_name
from
    Orders o
    left join Customers c on o.customer_id = c.customer_id
group by 
    o.customer_id, 
    c.customer_name
having sum((o.product_name = 'A')::INT) > 0
    and sum((o.product_name = 'B')::INT) > 0
    and sum((o.product_name = 'C')::INT) = 0
order by o.customer_id