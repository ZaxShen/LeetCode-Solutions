-- Last updated: 8/4/2025, 10:44:01 PM
select
    product_id,
    "store1" as store,
    store1 as price
from Products
where store1 is not null
union
select
    product_id,
    "store2" as store,
    store2 as price
from Products
where store2 is not null
union
select
    product_id,
    "store3" as store,
    store3 as price
from Products
where store3 is not null;