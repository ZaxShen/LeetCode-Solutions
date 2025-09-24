select
    contest_id,
    round(count(*)::numeric / (select count(*) from Users) * 100, 2) as percentage
from register
group by contest_id
order by
    percentage desc, contest_id asc