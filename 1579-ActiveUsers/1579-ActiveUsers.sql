-- Last updated: 8/4/2025, 10:45:07 PM
with cte as
	(
	select
		id, login_date,
		row_number() over(partition by id order by login_date) as rn
	from (select distinct id, login_date from Logins) as distinct_logins
    )
select distinct cte.id, `name` -- may have same users
from cte
inner join Accounts using(id)
group by 1, login_date - interval rn day -- may have same user with continusous but less than 5 records
having count(*) >= 5
order by 1;