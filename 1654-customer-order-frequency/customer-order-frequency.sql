with cte as (
    select
        o.customer_id,
        c.name,
        to_char(o.order_date, 'YYYY-MM') as order_month,
        sum(o.quantity * p.price) as total
    from
        Orders o
        left join Customers c on o.customer_id = c.customer_id
        left join Product p on o.product_id = p.product_id
    where o.order_date between '2020-06-01'::DATE and '2020-07-31'::DATE
    group by o.customer_id, c.name, to_char(o.order_date, 'YYYY-MM')
)
select
    customer_id,
    name
from cte
group by customer_id, name
    having count(*) = 2
    and min(total) >= 100