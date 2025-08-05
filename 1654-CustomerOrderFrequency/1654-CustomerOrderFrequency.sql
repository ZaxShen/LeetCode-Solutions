-- Last updated: 8/4/2025, 10:44:28 PM
/*Select the the customers who spent at least $100 in each month of June and July 2020.
- Customers PK: customer_id
- Product PK: product_id
- Orders PK: order_id

- SOLUTION: JOIN, GROUP BY
*/
with cte as
(
	select
		distinct(o.customer_id) as customer_id,
		c.name,
		date_format(order_date, '%Y-%m') as date,
		sum(quantity * price) as total
	from Orders o
	left join Product p using(product_id)
	left join Customers c using(customer_id)
	where date_format(order_date, '%Y-%m') between '2020-06' and '2020-07'
	group by 1, 2, 3
)
select customer_id, `name`
from cte
where total >= 100
group by 1, 2
having count(*) = 2;