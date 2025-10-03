WITH latest_prices AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rn
    FROM Products
    WHERE change_date <= '2019-08-16'
),
all_products AS (
    SELECT DISTINCT product_id 
    FROM Products
)
SELECT
    ap.product_id,
    COALESCE(lp.new_price, 10) as price
FROM all_products ap
LEFT JOIN latest_prices lp 
    ON ap.product_id = lp.product_id 
    AND lp.rn = 1;