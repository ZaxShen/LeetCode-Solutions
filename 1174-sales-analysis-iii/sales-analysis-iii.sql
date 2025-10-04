select
    s.product_id,
    p.product_name
from Sales s
    join Product p on s.product_id = p.product_id
group by
    s.product_id,
    p.product_name
having
    count(*) filter(where s.sale_date between '2019-01-01' and '2019-03-31') > 0
    and count(*) filter(where s.sale_date < '2019-01-01') = 0
    and count(*) filter(where s.sale_date > '2019-03-31') = 0
