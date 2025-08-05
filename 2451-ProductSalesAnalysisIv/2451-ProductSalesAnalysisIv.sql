-- Last updated: 8/4/2025, 10:43:33 PM
with cte as (
select
    s.user_id,
    s.product_id,
    dense_rank() over(partition by user_id order by sum(s.quantity * p.price) desc) as amount_rnk
from Sales s
join Product p using(product_id)
group by user_id, product_id
)
select user_id, product_id
from cte
where amount_rnk = 1