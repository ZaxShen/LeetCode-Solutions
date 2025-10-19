with cte as (
    select 
        TO_CHAR(trans_date, 'YYYY-MM') as month, 
        country, 
        amount, 
        state
    from Transactions
    where state = 'approved'
    union all
    select 
        TO_CHAR(c.trans_date, 'YYYY-MM') as month, 
        t.country, 
        t.amount, 
        'chargeback' as state
    from Chargebacks c
    join Transactions t on c.trans_id = t.id
)
select
    month,
    country,
    sum((state = 'approved')::INT) as approved_count,
    sum(case when state = 'approved' then amount else 0 end) as approved_amount,
    sum((state = 'chargeback')::INT) as chargeback_count,
    sum(case when state = 'chargeback' then amount else 0 end) as chargeback_amount
from cte
group by month, country
order by month, country