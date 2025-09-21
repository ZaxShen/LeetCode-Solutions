-- Write your PostgreSQL query statement below
select Country.name as country
from Calls
join Person
    on Person.id in (Calls.caller_id, Calls.callee_id)
join Country
    on SUBSTRING(Person.phone_number, 1, 3) = Country.country_code
group by Country.name
having avg(duration) > (select avg(duration) from Calls)