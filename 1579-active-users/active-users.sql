with cte as (
    select
        id,
        login_date - interval '1 day' * row_number() over(partition by id order by login_date) as grp
    from (select distinct * from Logins)
)
select distinct
    c.id,
    a.name
from
    cte c
    left join Accounts a on c.id = a.id
group by c.id, a.name, c.grp
having count(c.id) >= 5
order by c.id