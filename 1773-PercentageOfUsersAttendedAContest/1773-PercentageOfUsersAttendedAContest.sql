-- Last updated: 8/4/2025, 10:44:18 PM
# Write your MySQL query statement below
with cte as (
-- Make the table with all the combinations
select distinct contest_id, u.user_id
from Register r
cross join Users u
order by 1 asc
)
select cte.contest_id, round(count(r.user_id) / count(cte.contest_id) * 100, 2) as percentage
from cte
left join Register r
	on cte.contest_id = r.contest_id
    and cte.user_id = r.user_id
group by 1
order by 2 desc, 1 asc;