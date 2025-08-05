-- Last updated: 8/4/2025, 10:43:51 PM
with cte as
    (
    select
        r1.user_id as user1_id,
        r2.user_id as user2_id,
        dense_rank() over(order by count(r1.follower_id) desc) as dr_common_followers
    from Relations r1
    inner join Relations r2 on r1.follower_id = r2.follower_id
        and r1.user_id < r2.user_id
    group by r1.user_id, r2.user_id
    order by 3 desc
    )
select user1_id, user2_id
from cte
where dr_common_followers = 1;