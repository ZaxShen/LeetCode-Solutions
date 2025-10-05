select
    order_date,
    round(avg((order_date = customer_pref_delivery_date)::INT) * 100, 2) as immediate_percentage
from Delivery
group by order_date
order by order_date
