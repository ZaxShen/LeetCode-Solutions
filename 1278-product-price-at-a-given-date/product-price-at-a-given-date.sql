with cte as (
    select
        *,
        dense_rank() over(partition by product_id order by change_date desc) as change_date_desc
    from Products
    where change_date <= '2019-08-16'::DATE
)
select product_id, new_price as price
from cte
where change_date_desc = 1
union
select product_id, 10 as price
from Products
where product_id not in (select product_id from cte)