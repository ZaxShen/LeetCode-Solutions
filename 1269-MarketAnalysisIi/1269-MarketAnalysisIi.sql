-- Last updated: 8/4/2025, 10:45:54 PM
WITH SecondSold AS (
    SELECT
        order_id,
        seller_id,
        item_id,
        DENSE_RANK() OVER (
            PARTITION BY seller_id
            ORDER BY order_date ASC
        ) AS order_date_rnk
    FROM Orders
)
SELECT
    u.user_id AS seller_id,
    CASE WHEN i.item_brand = u.favorite_brand THEN 'yes' ELSE 'no' END AS "2nd_item_fav_brand"
FROM
    Users u
    LEFT JOIN SecondSold s ON u.user_id = s.seller_id AND s.order_date_rnk = 2
    LEFT JOIN Items i ON s.item_id = i.item_id;