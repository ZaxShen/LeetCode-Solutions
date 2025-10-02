with cte as (
    select
        r1.user_id as user1_id,
        r2.user_id as user2_id,
        dense_rank() over(order by count(*) desc) as followers_desc
    from Relations r1
        -- join Relations r2 using (follower_id)
        join Relations r2 on r1.follower_id = r2.follower_id
            and r1.user_id < r2.user_id
    group by
        r1.user_id,
        r2.user_id
)
select
    user1_id,
    user2_id
from cte
where followers_desc = 1
