with cte1 as (
    select
        user_id,
        credit
    from Users
    union all
    select
        paid_by,
        -amount
    from Transactions
    union all
    select
        paid_to,
        amount
    from Transactions
), cte2 as (
select
    u.user_id,
    u.user_name,
    sum(coalesce(c.credit, u.credit)) as credit
from
    Users u
    left join cte1 c on u.user_id = c.user_id
group by u.user_id, u.user_name
)
select
    *,
    case
        when credit < 0 then 'Yes'
        else 'No'
    end as credit_limit_breached
from cte2