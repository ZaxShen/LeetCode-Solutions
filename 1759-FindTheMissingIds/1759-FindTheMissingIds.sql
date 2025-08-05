-- Last updated: 8/4/2025, 10:44:19 PM
with recursive
cte as
	(
    select 1 as ids
    union all
    select ids + 1
    from cte
    where ids < (select max(customer_id) from Customers)
    )
select ids
from cte
where ids not in (select customer_id from Customers);