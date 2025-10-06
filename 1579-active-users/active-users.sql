with cte as (
    select
        id,
        login_date - interval '1 day' * row_number() over(partition by id order by login_date) as grp
    from (select distinct id, login_date from Logins)
)
select distinct
    cte.id,
    a.name
from
    cte
    join Accounts a on cte.id = a.id
group by cte.id, a.name, grp
    having count(grp) >= 5
order by cte.id
