with cte as (
    select
        visited_on,
        sum(amount) as daily_total,
        sum(sum(amount)) over(order by visited_on rows between 6 preceding and current row) as rolling_sum_7day,
        round(avg(sum(amount)) over(order by visited_on rows between 6 preceding and current row), 2) as rolling_avg_7day,
        row_number() over(order by visited_on) as day_num
    from Customer
    group by visited_on
)
select
    visited_on,
    rolling_sum_7day as amount,
    rolling_avg_7day as average_amount
from cte
where day_num >= 7
