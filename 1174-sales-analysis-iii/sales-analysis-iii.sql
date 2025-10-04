select
    s.product_id,
    p.product_name
from Sales s
    join Product p on s.product_id = p.product_id
group by
    s.product_id,
    p.product_name
having
    MIN(s.sale_date) >= '2019-01-01'
    and max(s.sale_date) <= '2019-03-31'
