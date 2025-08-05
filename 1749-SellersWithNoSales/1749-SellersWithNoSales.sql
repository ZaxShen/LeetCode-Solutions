-- Last updated: 8/4/2025, 10:44:20 PM
# Write your MySQL query statement below
select seller_name
from Orders o
right join Seller using(seller_id)
where seller_id not in
    (select seller_id from Orders where year(sale_date) = 2020)
order by 1;