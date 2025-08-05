-- Last updated: 8/4/2025, 10:45:40 PM
# Write your MySQL query statement below
select p.product_id, ifnull(round(sum(price * units) / sum(units), 2), 0) as average_price
from Prices p
left join UnitsSold u
    on p.product_id = u.product_id
    and p.start_date <= u.purchase_date
    and u.purchase_date <= p.end_date
group by p.product_id