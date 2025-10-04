with cte as (
    select
        seller_id,
        dense_rank() over(order by sum(price) desc) as amount_desc
    from Sales
    group by seller_id
)
select seller_id
from cte
where amount_desc = 1