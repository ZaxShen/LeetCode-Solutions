select
    t.request_at::date as day,
    round(count(*) filter (where t.status ~ '^cancelled')::decimal / count(*), 2) as "Cancellation Rate"
from trips t
    join users clients on t.client_id = clients.users_id 
        and clients.role = 'client' 
        and clients.banned = 'No'
    join users drivers on t.driver_id = drivers.users_id 
        and drivers.role = 'driver' 
        and drivers.banned = 'No'
where t.request_at::date between '2013-10-01' and '2013-10-03'
group by t.request_at