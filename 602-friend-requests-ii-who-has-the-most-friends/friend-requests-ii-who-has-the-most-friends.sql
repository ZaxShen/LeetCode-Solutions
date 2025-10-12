with cte(id, friend_id) as (
    select requester_id, accepter_id from RequestAccepted
    union
    select accepter_id, requester_id from RequestAccepted
)
select id, count(friend_id) as num
from cte
group by id
order by num desc
limit 1