-- product_id is PK of Product, and FK of Sales
-- product_id, product_name, sale_date; quantity may be zero all null?
-- filter Sales finally join Product to opt

with cte as (
select
    s.product_id
from Sales s
group by s.product_id
having
    min(s.sale_date) >= '2019-01-01'::DATE
    and max(s.sale_date) < '2019-04-01'::DATE
)
select cte.product_id, p.product_name
from cte
join Product p on cte.product_id = p.product_id