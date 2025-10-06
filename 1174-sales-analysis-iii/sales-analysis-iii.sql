select
    s.product_id,
    p.product_name
from
    Sales s
    left join Product p on s.product_id = p.product_id
group by s.product_id, p.product_name
having min(s.sale_date) >= '2019-01-01'::DATE
    and max(s.sale_date) <= '2019-03-31'::DATE