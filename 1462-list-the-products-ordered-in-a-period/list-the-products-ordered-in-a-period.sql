select
    p.product_name,
    sum(unit) as unit
from
    Orders o
    join Products p on o.product_id = p.product_id
where to_char(o.order_date, 'YYYY-MM') = '2020-02'
group by p.product_name
    having sum(unit) >= 100