with cte as (
    select
        o.customer_id,
        o.product_id,
        p.product_name,
        dense_rank() over(partition by o.customer_id order by count(o.order_id) desc) as order_count_desc
    from
        Orders o
        join Customers c on o.customer_id = c.customer_id
        join Products p on o.product_id = p.product_id
    group by o.customer_id, o.product_id, p.product_name
)
select
    customer_id,
    product_id,
    product_name
from cte
where order_count_desc = 1
ORDER BY
    product_name,
    product_id,
    customer_id
