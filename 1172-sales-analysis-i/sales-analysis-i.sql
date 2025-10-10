with cte as (
select
    seller_id,
    dense_rank() over(order by sum(price) desc) as total_price_desc
from Sales
group by seller_id
)
select seller_id
from cte where total_price_desc = 1