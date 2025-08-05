-- Last updated: 8/5/2025, 12:18:59 AM
select
    sell_date,
    count(distinct product) as num_sold,
    group_concat(distinct product order by product asc separator ',') as products
from Activities
group by sell_date
order by sell_date