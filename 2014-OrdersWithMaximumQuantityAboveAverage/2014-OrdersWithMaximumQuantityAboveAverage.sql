-- Last updated: 8/4/2025, 10:43:56 PM
# Write your MySQL query statement below
with cte as
	(
	select order_id, avg(quantity) as avg_quantity
	from OrdersDetails
	group by order_id
	)
select distinct order_id
from OrdersDetails
where quantity > (select max(avg_quantity) from cte);