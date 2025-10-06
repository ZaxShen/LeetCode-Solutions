select s.seller_name
from
    Seller s
    left join Orders o on s.seller_id = o.seller_id
where s.seller_id not in (
    select seller_id
    from Orders
    where extract(year from sale_date) = 2020
)
order by seller_name