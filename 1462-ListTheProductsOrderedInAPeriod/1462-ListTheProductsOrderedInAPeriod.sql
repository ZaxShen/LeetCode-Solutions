-- Last updated: 8/4/2025, 10:45:31 PM
select product_name, sum(unit) as unit
from Products
left join Orders using (product_id)
where date_format(order_date, '%Y-%m') = '2020-02'
group by 1
having sum(unit) >= 100