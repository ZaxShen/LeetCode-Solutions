select
    user_id,
    "name",
    mail
from Users
-- where mail ~ '^[[:alpha:]][[:alnum:]_.-]*(@leetcode\.com)$'
WHERE mail ~ '^[a-zA-Z][A-Za-z0-9_.-]*@leetcode\.com$'