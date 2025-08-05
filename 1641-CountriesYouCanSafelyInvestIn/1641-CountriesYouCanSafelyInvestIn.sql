-- Last updated: 8/4/2025, 10:44:29 PM
# Write your MySQL query statement below
select co.name as country
from person p
inner join country co on substring(phone_number,1,3) = country_code
inner join calls c on p.id in (c.caller_id, c.callee_id)
group by co.name
having avg(duration) > (select avg(duration) from calls);