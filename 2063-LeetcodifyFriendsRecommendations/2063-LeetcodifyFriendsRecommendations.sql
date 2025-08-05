-- Last updated: 8/4/2025, 10:43:52 PM
# Write your MySQL query statement below
with cte as 
	(
    select 
		l1.user_id as uid1, 
        l2.user_id as uid2
    from Listens l1
	inner join Listens l2 on l1.day = l2.day 
		and l1.song_id = l2.song_id 
		and l1.user_id != l2.user_id
    group by l1.user_id, l2.user_id, l1.day
    having count(distinct l1.song_id) >= 3
	), 
    f (uid1, uid2) as 
    (
    select user1_id, user2_id from Friendship
    union
    select user2_id, user1_id from Friendship
	)
select 
	uid1 as user_id, 
    uid2 as recommended_id
from cte
where (uid1, uid2) not in (select uid1, uid2 from f)
group by uid1, uid2;