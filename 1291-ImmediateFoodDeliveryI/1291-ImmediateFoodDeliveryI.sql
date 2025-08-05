-- Last updated: 8/4/2025, 10:45:52 PM
select round(avg(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
from Delivery;