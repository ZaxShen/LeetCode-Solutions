select
    s.buyer_id
from Sales s
join Product p on s.product_id = p.product_id
group by s.buyer_id
    having count(*) filter(where p.product_name = 'S8') > 0
    and count(*) filter(where p.product_name = 'iPhone') = 0