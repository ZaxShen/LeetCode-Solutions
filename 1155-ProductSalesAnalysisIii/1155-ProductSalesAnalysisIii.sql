-- Last updated: 8/4/2025, 10:46:17 PM
with cte as (
    select s.product_id, `year`, dense_rank() over(partition by s.product_id order by `year` asc) as year_rnk, quantity, price
    from Sales s
    inner join Product using (product_id)
)
select product_id, `year` as first_year,  quantity, price
from cte
where year_rnk = 1;