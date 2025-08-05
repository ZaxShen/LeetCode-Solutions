-- Last updated: 8/4/2025, 10:43:30 PM
select order_date, round(avg(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
from Delivery
group by order_date
order by order_date