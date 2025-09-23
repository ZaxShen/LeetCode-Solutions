select
    sell_date,
    count(distinct product) as num_sold,
    string_agg(distinct product, ',' order by product asc) as products
from activities
group by sell_date