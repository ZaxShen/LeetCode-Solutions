-- Last updated: 8/4/2025, 10:44:14 PM
select
    `name`, 
    ifnull(sum(rest), 0) as rest, 
    ifnull(sum(paid), 0) as paid, 
    ifnull(sum(canceled), 0) as canceled, 
    ifnull(sum(refunded), 0) as refunded
from Product
left join Invoice using(product_id)
group by 1
order by 1;
