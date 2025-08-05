-- Last updated: 8/4/2025, 10:45:44 PM
# Write your MySQL query statement below
with cte as
(
	select
		host_team as team_id,
		case 
			when host_goals > guest_goals then 3
			when host_goals < guest_goals then 0
			else 1
		end as num_points
	from Matches
	union all
	select
		guest_team as team_id,
		case 
			when host_goals > guest_goals then 0
			when host_goals < guest_goals then 3
			else 1
		end as num_points
	from Matches
)
select team_id, team_name, ifnull(sum(num_points), 0) as num_points
from Teams
left join cte using(team_id)
group by 1, 2
order by 3 desc, 1 asc;