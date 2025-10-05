with all_transactions as (
    select
        to_char(trans_date, 'YYYY-MM') as month,
        country,
        'approved' as "state",
        amount
    from Transactions t
    where "state" = 'approved'

    union all

    select
        to_char(c.trans_date, 'YYYY-MM') as month,
        t.country,
        'chargeback' as "state",
        t.amount
    from Chargebacks c
        join Transactions t on c.trans_id = t.id
)
-- select * from all_transactions
select
    month,
    country,
    sum(case when "state" = 'approved' then 1 else 0 end) as approved_count,
    sum(case when "state" = 'approved' then amount else 0 end) as approved_amount,
    sum(case when "state" = 'chargeback' then 1 else 0 end) as chargeback_count,
    sum(case when "state" = 'chargeback' then amount else 0 end) as chargeback_amount
from all_transactions
group by month, country
order by month, country