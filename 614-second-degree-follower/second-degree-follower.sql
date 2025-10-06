select
    followee as follower,
    count(follower) as num
from Follow
where followee in (select distinct follower from Follow)
group by followee
order by follower