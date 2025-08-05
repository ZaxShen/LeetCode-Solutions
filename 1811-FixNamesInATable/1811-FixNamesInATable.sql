-- Last updated: 8/4/2025, 10:44:15 PM
select
    user_id,
    concat(upper(substring(name, 1, 1)), lower(substring(name, 2))) as name
from Users
order by user_id