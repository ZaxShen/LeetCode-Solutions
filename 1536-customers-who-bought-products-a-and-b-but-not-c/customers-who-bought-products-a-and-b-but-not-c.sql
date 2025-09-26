select
    c.customer_id,
    c.customer_name
from Customers c
    left join Orders o using(customer_id)
group by
    c.customer_id,
    c.customer_name
    having sum(case when product_name = 'A' then 1 else 0 end) > 0
        and sum(case when product_name = 'B' then 1 else 0 end) > 0
        and sum(case when product_name = 'C' then 1 else 0 end) = 0
order by c.customer_id