-- with cte(call_id, duration) as (
--     select caller_id, duration from Calls
--     union all
--     select callee_id, duration from Calls
-- )
-- select
--     co.name as country
-- from
--     cte c
--     join Person p on c.call_id = p.id
--     join Country co on substring(p.phone_number, 1, 3) = co.country_code
-- group by co.name
--     having avg(duration) > (select avg(duration) from Calls)

SELECT
    co.name AS country
    -- *
FROM
    Calls ca
    JOIN Person p ON p.id IN (ca.caller_id, ca.callee_id)
    JOIN Country co ON SUBSTRING(p.phone_number, 1, 3) = co.country_code
GROUP BY co.name
HAVING AVG(duration) > (SELECT AVG(duration) FROM Calls)