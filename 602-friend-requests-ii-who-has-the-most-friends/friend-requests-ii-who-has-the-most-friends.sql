with cte(id) as (
    select 
        requester_id as id
    from RequestAccepted
    union all
    select
        accepter_id
    from RequestAccepted
)
select id, count(id) as num
from cte
group by id
order by num desc
limit 1