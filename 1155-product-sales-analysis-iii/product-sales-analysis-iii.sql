with cte as (
    select
        product_id,
        min(year) as year
    from Sales
    group by product_id
)
select
    cte.product_id,
    cte.year as first_year,
    s.quantity,
    s.price
from cte
    join Sales s on cte.product_id = s.product_id
        and cte.year = s.year