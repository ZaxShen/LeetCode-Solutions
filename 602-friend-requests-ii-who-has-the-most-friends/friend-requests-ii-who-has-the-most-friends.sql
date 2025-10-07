with cte as (
    select 
        requester_id as id,
        accepter_id as friend_id
    from RequestAccepted
    union
    select
        accepter_id as id,
        requester_id as friend_id
    from RequestAccepted
)
select id, count(friend_id) as num
from cte
group by id
order by num desc
limit 1