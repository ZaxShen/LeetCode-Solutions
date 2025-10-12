with cte as (
    select
        *,
        dense_rank() over(partition by customer_id order by order_date) as order_rnk
    from Delivery
)
select round(avg((order_date = customer_pref_delivery_date)::INT) * 100, 2) as immediate_percentage
from cte
where order_rnk = 1