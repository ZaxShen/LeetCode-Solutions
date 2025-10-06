select buyer_id
from
    Sales s
    join Product p on s.product_id = p.product_id
group by buyer_id
having sum((p.product_name = 'S8')::INT) != 0
    and sum((p.product_name = 'iPhone')::INT) = 0