select country.name as country
from calls
join person on person.id in (calls.caller_id, calls.callee_id)
join country on substring(person.phone_number, 1, 3) = country.country_code
group by country.name
having avg(duration) > (select avg(duration) from calls)