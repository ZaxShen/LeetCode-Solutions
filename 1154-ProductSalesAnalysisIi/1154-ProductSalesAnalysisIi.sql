-- Last updated: 8/4/2025, 10:46:18 PM
select product_id, sum(quantity) as total_quantity
from Sales
group by 1;