with cte as (
select
    p.product_name,
    o.product_id,
    o.order_id,
    o.order_date,
    dense_rank() over(partition by o.product_id order by o.order_date desc) as order_date_desc
from
    Orders o
    join Products p on o.product_id = p.product_id
)
select
    product_name,
    product_id,
    order_id,
    order_date
from cte
where order_date_desc = 1
order by
    product_name,
    product_id,
    order_id