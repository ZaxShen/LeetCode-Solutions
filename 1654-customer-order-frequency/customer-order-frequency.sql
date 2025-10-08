with cte as (
    select
        o.customer_id,
        -- date_trunc('month', o.order_date) as year_month,
        sum(p.price * o.quantity) as amount
    from
        Orders o
        join Product p on o.product_id = p.product_id
    where o.order_date between '2020-06-01'::DATE and '2020-07-31'::DATE
    group by 
        customer_id, 
        date_trunc('month', o.order_date)
)
select
    cte.customer_id,
    c.name
from 
    cte
    join customers c on cte.customer_id = c.customer_id
where cte.amount >= 100
group by
    cte.customer_id,
    c.name
having count(*) >= 2