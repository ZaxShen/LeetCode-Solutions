select
    t.request_at as Day,
    round(count(*) FILTER (where t.status ~ '^cancelled')::NUMERIC / count(*), 2) as "Cancellation Rate"
from Trips t
    join Users c on t.client_id = c.users_id
        and c.banned = 'No'
        and c.role = 'client'
    join Users d on t.driver_id = d.users_id
        and d.banned = 'No'
        and d.role = 'driver'
where t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at