select
    t.request_at::date as day,
    round(count(*) filter(where t.status like 'cancelled%')::decimal / count(*), 2) as "Cancellation Rate"
from trips t
    join users clients
        on t.client_id = clients.users_id
        and clients.banned = 'No'
        and clients.role = 'client'
    join users drivers
        on t.driver_id = drivers.users_id
        and drivers.banned = 'No'
        and drivers.role = 'driver'
where t.request_at::date between '2013-10-01' and '2013-10-03'
group by t.request_at::date