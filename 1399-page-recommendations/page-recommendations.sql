with cte as (
    select
        least(user1_id, user2_id) as user1_id,
        greatest(user1_id, user2_id) as user2_id
    from Friendship
)
select distinct l.page_id as recommended_page
from
    cte c
    join Likes l on c.user2_id = l.user_id
where c.user1_id = 1
    and l.page_id not in (
        select page_id from Likes where user_id = 1
    )