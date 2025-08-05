-- Last updated: 8/4/2025, 10:43:50 PM
# Write your MySQL query statement below
with friends as
(
	select user1_id, user2_id
	from Friendship
	union
	select user2_id, user1_id
	from Friendship
)
select 
    f1.user1_id, 
    f1.user2_id,
    count(f3.user2_id) as common_friend
from Friendship f1
inner join friends f2 on f1.user1_id = f2.user1_id # user1_id's friends
inner join friends f3 on f1.user2_id = f3.user1_id # user2_id's friends
	and f2.user2_id = f3.user2_id # common friends
group by 1, 2
having common_friend >= 3;