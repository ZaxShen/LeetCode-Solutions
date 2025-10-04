select
    s.buyer_id
from Sales s
    join Product p on s.product_id = p.product_id
group by s.buyer_id
having COUNT(*) filter (where product_name = 'iPhone') = 0
    and COUNT(*) filter (where product_name = 'S8') > 0