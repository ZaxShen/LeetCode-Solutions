with medals(contest_id, user_id) as (
    select contest_id, gold_medal from Contests
    union all
    select contest_id, silver_medal from Contests
    union all
    select contest_id, bronze_medal from Contests
),
grps as (
    select
        user_id,
        contest_id,
        contest_id - row_number() over(partition by user_id order by contest_id) as grp
    from medals
),
winners(user_id) as (
    select distinct user_id
    from grps
    group by user_id, grp
        having count(contest_id) >= 3
    union
    select gold_medal
    from Contests
    group by gold_medal
        having count(gold_medal) >= 3
)
select
    name,
    mail
from
    winners
    join Users using(user_id)
