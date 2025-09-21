select contest_id, round(count(*)::DECIMAL / (select count(user_id) from users) * 100, 2) as percentage
from register
group by contest_id
order by percentage desc, contest_id asc