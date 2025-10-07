with cte as (
    select user_id, credit from Users
    union all
    select paid_by, -amount from Transactions
    union all
    select paid_to, amount from Transactions
)
select
    c.user_id,
    u.user_name,
    sum(c.credit) as credit,
    CASE
        WHEN SUM(c.credit) < 0 then 'Yes'
        else 'No'
    END AS credit_limit_breached
from
    cte c
    join Users u on c.user_id = u.user_id
group by
    c.user_id,
    u.user_name
order by user_id