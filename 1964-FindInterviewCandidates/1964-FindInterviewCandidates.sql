-- Last updated: 8/4/2025, 10:43:59 PM
with medals as
	(
    select contest_id, gold_medal as user_id from Contests
    union all
    select contest_id, silver_medal as user_id from Contests
    union all
    select contest_id, bronze_medal as user_id from Contests
    ),
medals_by_users as
	(
	select
		user_id,
		contest_id,
        row_number() over(partition by user_id order by contest_id) as rn
	from medals
	),
user_ids as
	(
	select distinct user_id
	from medals_by_users
	group by 1, contest_id - rn
	having count(*) >= 3
	union
	select distinct gold_medal as user_id
	from Contests
	group by 1
	having count(gold_medal) >= 3
	)
select `name`, mail
from Users
inner join user_ids using(user_id);