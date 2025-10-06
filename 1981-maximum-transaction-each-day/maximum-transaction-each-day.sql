with cte as (
    select
        transaction_id,
        dense_rank() over(partition by to_char(day, 'YYYY-MM-DD') order by amount desc) as amount_desc
    from Transactions
)
select transaction_id
from cte
where amount_desc = 1
order by transaction_id