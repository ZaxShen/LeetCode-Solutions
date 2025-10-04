-- select
--     buyer_id,
--     join_date,
--     count(*) filter (where extract(year from order_date) = 2019) as orders_in_2019
-- from Users u
--     left join Orders o on u.user_id = o.buyer_id
-- group by buyer_id, join_date
-- order by buyer_id

select
    u.user_id as buyer_id,
    u.join_date,
    sum(case when extract(year from o.order_date) = 2019 then 1 else 0 end) as orders_in_2019
from Users u
    left join Orders o on u.user_id = o.buyer_id
group by u.user_id, u.join_date
order by u.user_id