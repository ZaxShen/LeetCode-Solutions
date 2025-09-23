with customer_spend as (
    select
        customer_id,
        name,
        date_trunc('month', order_date) as year_month,
        sum(price * quantity) as spend
    from orders
    join customers using(customer_id)
    join product using(product_id)
    where order_date >= '2020-06-01'
        and order_date < '2020-08-01'
    group by
        customer_id,
        name,
        date_trunc('month', order_date)
)
select customer_id, name
from customer_spend
where spend >= 100
group by customer_id, name
    having count(*) = 2 