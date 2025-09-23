select
    query_name,
    round(avg(rating::decimal / position), 2) as quality,
    round(avg((rating < 3)::integer) * 100, 2) as poor_query_percentage
from queries
group by query_name