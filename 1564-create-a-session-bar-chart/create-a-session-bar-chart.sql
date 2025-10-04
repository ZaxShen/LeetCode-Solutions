with bins as (
    select '[0-5>' as bin, 1 as bin_order
    union all select '[5-10>', 2
    union all select '[10-15>', 3
    union all select '15 or more', 4
),
categorized as (
    select
        *,
        case
            when duration/60 < 5 THEN '[0-5>'
            when duration/60 < 10 THEN '[5-10>'
            when duration/60 < 15 THEN '[10-15>'
            else '15 or more'
        end as bin
    from Sessions
)
select
    b.bin,
    count(c.session_id) as total
from bins b
left join categorized c on b.bin = c.bin
group by b.bin, b.bin_order
order by b.bin_order