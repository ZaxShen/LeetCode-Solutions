select
    u.user_id as buyer_id,
    u.join_date,
    count(*) filter(where extract(year from o.order_date) = 2019) as orders_in_2019
from
    Users u
    left join Orders o on u.user_id = o.buyer_id
group by u.user_id, u.join_date
