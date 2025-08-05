-- Last updated: 8/4/2025, 10:43:35 PM
select user_id, sum(quantity * price) as spending
from Sales
inner join Product using (product_id)
group by 1
order by 2 desc;