select
    s.buyer_id
from Sales s
    join Product p on s.product_id = p.product_id
group by s.buyer_id
having SUM((product_name = 'iPhone')::int) = 0
    and SUM((product_name = 'S8')::int) > 0