-- Last updated: 8/4/2025, 10:46:13 PM
select buyer_id
from sales s
join Product p on s.product_id = p.product_id
group by buyer_id
having SUM(p.product_name = 'S8') > 0
    and SUM(p.product_name = 'iPhone') = 0