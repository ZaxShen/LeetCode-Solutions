select
    coalesce(s.user_id, c.user_id) as user_id,
    round(coalesce(avg((c.action = 'confirmed')::int), 0), 2) as confirmation_rate
from 
    Signups s
    full outer join Confirmations c on s.user_id = c.user_id
group by 1