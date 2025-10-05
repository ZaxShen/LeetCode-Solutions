with salary_categories as (
    select 'Low Salary' as category
    union select 'Average Salary'
    union select 'High Salary'
), account_categories as (
    select
        case
            when income < 20000 then 'Low Salary'
            when income <= 50000 then 'Average Salary'
            else 'High Salary'
        end as category
    from Accounts
)
select
    s.category,
    count(a.category) as accounts_count
from
    salary_categories s
    left join account_categories a using (category)
group by category