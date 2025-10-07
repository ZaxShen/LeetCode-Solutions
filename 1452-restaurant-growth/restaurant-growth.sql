with cte as (
    select
        visited_on,
        sum(amount) as daily_amount
    from Customer
    group by visited_on
)
select
    visited_on,
    sum(daily_amount) over (
        order by visited_on
        rows between 6 preceding and current row
    ) as amount,
    round(avg(daily_amount) over (
        order by visited_on
        rows between 6 preceding and current row

    ), 2) as average_amount
from cte
offset 6