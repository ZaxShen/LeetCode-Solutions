select
    request_at as Day,
    round(count(*) filter (where t.status != 'completed')::DECIMAL / count(*), 2) as "Cancellation Rate"
from trips t
join users u1 on t.client_id = u1.users_id and u1.role = 'client' and u1.banned = 'No'
join users u2 on t.driver_id = u2.users_id and u2.role = 'driver' and u2.banned = 'No'
where request_at between '2013-10-01' and '2013-10-03'
group by Day
-- where Day::date between '2013-10-01' and '2013-10-03'
-- WHERE Day BETWEEN '2013-10-01' AND '2013-10-03'
-- WHERE CAST('2013-10-01' AS DATE) <= Day AND Day <= CAST('2013-10-03' AS DATE)
