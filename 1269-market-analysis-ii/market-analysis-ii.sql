with cte as (
    select
        seller_id,
        item_id,
        dense_rank() over(partition by seller_id order by order_date) as sell_date_rnk
    from Orders
)
select
    u.user_id as seller_id,
    case
        when i.item_brand = u.favorite_brand then 'yes'
        else 'no'
    end as "2nd_item_fav_brand"
from
    Users u
    left join cte c on u.user_id = c.seller_id
        and c.sell_date_rnk = 2
    left join Items i on c.item_id = i.item_id
order by seller_id