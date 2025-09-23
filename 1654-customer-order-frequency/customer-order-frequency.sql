with customer_spend as (
select
    c.customer_id,
    c.name,
    sum(p.price * o.quantity) as spend,
    date_trunc('month', o.order_date) as year_month
from orders o
    join customers c using(customer_id)
    join product p using(product_id)
where
    order_date >= '2020-06-01'::date
    and order_date < '2020-08-01'::date
group by
    c.customer_id,
    c.name,
    date_trunc('month', o.order_date)
    having sum(p.price * o.quantity) >= 100
)
select customer_id, name
from customer_spend
group by customer_id, name
    having count(*) = 2;