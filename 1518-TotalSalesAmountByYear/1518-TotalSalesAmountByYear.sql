-- Last updated: 8/4/2025, 10:45:23 PM
# Write your MySQL query statement below
with recursive
all_dates as
    (
    select min(period_start) as sale_date
    from Sales
    union
    select sale_date + interval 1 day
    from all_dates
    where sale_date <= (select max(period_end) from Sales)
    )
select
    product_id,
    product_name,
    date_format(sale_date, "%Y") as report_year,
    sum(average_daily_sales) as total_amount
from Sales
inner join Product using(product_id)
inner join all_dates on period_start <= sale_date
    and sale_date <= period_end
group by 1, 2, 3
order by 1, 2;