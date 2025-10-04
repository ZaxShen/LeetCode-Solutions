with sec_item_sold as (
    select
        seller_id,
        order_date,
        item_id,
        dense_rank() over(partition by seller_id order by order_date) as order_date_asc
    from Orders
)
select
    u.user_id as seller_id,
    case
        when u.favorite_brand = i.item_brand then 'yes'
        else 'no'
    end as "2nd_item_fav_brand"
from Users u
    left join sec_item_sold s on u.user_id = s.seller_id
        and s.order_date_asc = 2
    left join Items i on s.item_id = i.item_id
order by u.user_id