-- Last updated: 8/4/2025, 10:45:51 PM
# Write your MySQL query statement below
with cte as
(
    select
        customer_id,
        order_date,
        customer_pref_delivery_date,
        rank() over(partition by customer_id order by order_date asc) as order_rnk
    from Delivery
)
select round(avg(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
from cte
where order_rnk = 1