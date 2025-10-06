select
    p.product_name,
    sum(o.unit) as unit
from
    Orders o
    left join Products p on o.product_id = p.product_id
where to_char(o.order_date, 'YYYY-MM') = '2020-02'
group by o.product_id, p.product_name
having sum(o.unit) >= 100