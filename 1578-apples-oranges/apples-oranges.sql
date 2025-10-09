with cte(sale_date, amount) as (
    select sale_date, sold_num from Sales where fruit = 'apples'
    union all
    select sale_date, -sold_num from Sales where fruit = 'oranges'
)
select
    sale_date,
    sum(amount) as diff
from cte
group by sale_date
order by sale_date