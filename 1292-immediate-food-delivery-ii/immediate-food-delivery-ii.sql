WITH cte AS (
    SELECT DISTINCT ON (customer_id)
        customer_id,
        order_date,
        customer_pref_delivery_date
    FROM Delivery
    ORDER BY customer_id, order_date
)
SELECT 
    ROUND(AVG((order_date = customer_pref_delivery_date)::INT) * 100, 2) AS immediate_percentage
FROM cte