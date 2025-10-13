with cte as (
    select
        *,
        row_number() over(partition by product_id order by year) as rn
    from Sales
)
select
    s.product_id,
    s.year as first_year,
    s.quantity,
    s.price
from 
    Sales s
    join cte c on s.product_id = c.product_id
    and s.year = c.year
where rn = 1