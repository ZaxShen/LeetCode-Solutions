with cte as (
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
select
    t.team_id,
    t.team_name,
    coalesce(sum(num_points), 0) as num_points
from
    Teams t
    left join cte c on t.team_id = c.team_id
group by t.team_id, t.team_name
order by num_points desc, team_id asc