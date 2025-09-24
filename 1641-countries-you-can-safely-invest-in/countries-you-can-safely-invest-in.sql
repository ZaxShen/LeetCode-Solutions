select co.name as country
from Calls ca
    join Person p on p.id in (ca.caller_id, ca.callee_id)
    join Country co on co.country_code = SUBSTRING(p.phone_number, 1, 3)
group by co.name
    having avg(ca.duration) > (select avg(duration) from Calls)