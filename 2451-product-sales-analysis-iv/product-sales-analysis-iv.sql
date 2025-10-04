with cte as (
    select
        s.user_id,
        s.product_id,
        dense_rank() over(partition by s.user_id order by sum(s.quantity * p.price) desc) as amount_desc
    from Sales s
        join Product p on s.product_id = p.product_id
    group by
        s.user_id,
        s.product_id
)
select
    user_id,
    product_id
from cte
where amount_desc = 1