with bins(bin, "order") as (
select '[0-5>', 1
union
select '[5-10>', 2
union
select '[10-15>', 3
union
select '15 or more', 4
), stats as (
select
    case
        when duration / 60 < 5 then '[0-5>'
        when duration / 60 < 10 then '[5-10>'
        when duration / 60 < 15 then '[10-15>'
        else '15 or more'
    end as bin
from Sessions
)
select
    b.bin,
    count(s.bin) as total
from bins b
left join stats s on b.bin = s.bin
group by b.bin, b."order"
order by b."order"
