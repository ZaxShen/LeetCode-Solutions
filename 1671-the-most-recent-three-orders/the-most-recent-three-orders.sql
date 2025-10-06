with cte as (
    select
        c.name as customer_name,
        c.customer_id,
        o.order_id,
        o.order_date,
        dense_rank() over(partition by c.customer_id order by o.order_date desc) as order_date_desc
    from
        Customers c
        join Orders o on c.customer_id = o.customer_id
)
select
    customer_name,
    customer_id,
    order_id,
    order_date
from cte
where order_date_desc <= 3
order by
    customer_name,
    customer_id,
    order_date desc