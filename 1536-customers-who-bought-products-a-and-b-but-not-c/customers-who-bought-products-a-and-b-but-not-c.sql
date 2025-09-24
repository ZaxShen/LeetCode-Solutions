with required_products as (
    select distinct
        c.customer_id,
        c.customer_name,
        o.product_name
    from Customers c
    -- if there is product table, use it for completed grid
    cross join Orders o
),
customer_product_grid AS (
    select
        rp.customer_id,
        rp.customer_name,
        rp.product_name,
        count(o.product_name) > 0 as purchased
    from required_products rp
    left join Orders o on rp.customer_id = o.customer_id
        and rp.product_name = o.product_name
    group by rp.customer_id, rp.customer_name, rp.product_name
),
customer_summary as (
select
    customer_id,
    customer_name,
    bool_and(case when product_name in ('A', 'B') then purchased else true end) as bought_a_and_b,
    bool_or(case when product_name = 'C' then purchased else false end) as bought_c
from customer_product_grid
group by customer_id, customer_name
order by customer_id
)
select customer_id, customer_name
from customer_summary
where bought_a_and_b is true
    and bought_c is false