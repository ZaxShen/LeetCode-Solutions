select seller_name
from Seller
where not exists (
    select 1
    from Orders
    where extract(year from sale_date) = 2020
    and Seller.seller_id = Orders.seller_id
)
order by seller_name