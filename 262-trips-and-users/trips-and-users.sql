with unbanned_clients as (
    select users_id
    from Users
    where banned = 'No' and role = 'client'
),
unbanned_drivers as (
    select users_id
    from Users
    where banned = 'No' and role = 'driver' 
)
select
    request_at as Day,
    round(count(*) filter(where status ~ '^cancelled')::NUMERIC / count(*), 2) as "Cancellation Rate"
from Trips t
where request_at::DATE between '2013-10-01'::DATE and '2013-10-03'::DATE
    and exists (select 1 from unbanned_clients uc where t.client_id = uc.users_id)
    and exists (select 1 from unbanned_drivers ud where t.driver_id = ud.users_id)
group by request_at