-- Last updated: 8/4/2025, 10:45:39 PM
# Write your MySQL query statement below
with cte as
    (
    select user1_id, user2_id
    from Friendship
    union all
    select user2_id, user1_id
    from Friendship
    )
select distinct(page_id) as recommended_page
from cte
inner join Likes on user2_id = user_id
where user1_id = 1
    and page_id not in (select page_id from Likes where user_id = 1);