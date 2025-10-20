with cte as (
    select
        customer_number,
        dense_rank() over(order by count(order_number) desc) as orders_rnk
    from Orders
    group by customer_number
)
select customer_number
from cte
where orders_rnk = 1