-- Last updated: 8/4/2025, 10:46:19 PM
select product_name, `year`, price
from Sales
left join Product using (product_id)