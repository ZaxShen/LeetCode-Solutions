-- Last updated: 8/4/2025, 10:46:14 PM
with cte as (
    select
        seller_id,
        price,
        rank() over(order by sum(price) desc) as price_rnk
    from Sales
    group by seller_id
)
select seller_id
from cte
where price_rnk = 1
