WITH CTE AS (
    select
        customer_id,
        min(order_date) as order_date
    from Delivery
    group by customer_id
)
SELECT ROUND(AVG((c.order_date = d.customer_pref_delivery_date)::INT) * 100, 2) AS immediate_percentage
FROM cte c
    join Delivery d on c.customer_id = d.customer_id
        and c.order_date = d.order_date