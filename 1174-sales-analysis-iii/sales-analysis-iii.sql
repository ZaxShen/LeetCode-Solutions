select distinct
    s1.product_id,
    p.product_name
from
    Sales s1
    join Product p on s1.product_id = p.product_id
where not exists (
    select 1
    from Sales s2
    where s1.product_id = s2.product_id
    and (s2.sale_date < '2019-01-01'::date or s2.sale_date >= '2019-04-01'::date)
)