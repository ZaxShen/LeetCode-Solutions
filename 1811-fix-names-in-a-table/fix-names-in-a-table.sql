select
    user_id,
    concat(UPPER(SUBstring(name, 1, 1)), lower(substring(name, 2))) as name
from Users
ORDER BY user_id