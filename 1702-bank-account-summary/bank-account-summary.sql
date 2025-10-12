with cte(user_id, credit) as (
    select user_id, credit from Users
    union all
    select paid_to, amount from Transactions
    union all
    select paid_by, -amount from Transactions
)

select
    u.user_id,
    u.user_name,
    sum(c.credit) as credit,
    case
        when sum(c.credit) > 0 then 'No'
        else 'Yes'
    end as credit_limit_breached
from
    cte c
    join Users u on c.user_id = u.user_id
group by u.user_id, u.user_name