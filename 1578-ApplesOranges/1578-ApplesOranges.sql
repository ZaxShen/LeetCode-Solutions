-- Last updated: 8/4/2025, 10:45:06 PM
# Write your MySQL query statement below
select
    s1.sale_date,
    s1.sold_num - s2.sold_num as diff
from Sales s1
inner join Sales s2 using(sale_date)
where s1.fruit = 'apples' and s2.fruit = 'oranges'
order by 1;