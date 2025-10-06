with cte as (
    select
        visited_on,
        sum(amount) as daily_total,
        sum(sum(amount)) over(order by visited_on rows between 6 preceding and current row) as rolling_sum_7d,
        avg(sum(amount)) over(order by visited_on rows between 6 preceding and current row) as rolling_avg_7d,
        row_number() over(order by visited_on) as num_day
    from Customer
    group by visited_on
)
select
    visited_on,
    rolling_sum_7d as amount,
    round(rolling_avg_7d, 2) as average_amount
from cte
where num_day >= 7