-- Last updated: 8/4/2025, 10:43:58 PM
# Teams PK: team_id
# Matches PK: home_team_id, away_team_id

with cte as
	(
	select
		home_team_id as team_id,
		home_team_goals as goal_for,
		away_team_goals as goal_against,
		home_team_goals - away_team_goals as goal_diff
	from Matches
	union all
	select
		away_team_id as team_id,
		away_team_goals as goal_for,
		home_team_goals as goal_against,
		away_team_goals - home_team_goals as goal_diff
	from Matches
	)
select
	team_name,
    count(*) as matches_played,
    sum(case when goal_diff > 0 then 3 when goal_diff < 0 then 0 else 1 end) as points,
    sum(goal_for) as goal_for,
    sum(goal_against) as goal_against,
    sum(goal_diff) as goal_diff
from cte
inner join Teams using(team_id)
group by 1
order by points desc, goal_diff desc, team_name asc;