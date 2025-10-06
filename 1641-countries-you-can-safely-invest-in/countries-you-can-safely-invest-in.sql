select co.name as country
from
    Calls ca
    join Person p on p.id in (ca.caller_id, ca.callee_id)
    join Country co on substring(p.phone_number, 1, 3) = co.country_code
group by country
having avg(duration) > (select avg(duration) from Calls)