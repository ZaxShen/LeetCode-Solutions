select
    query_name,
    round(avg(rating::numeric / position), 2) as quality,
    round(avg((rating < 3)::int) * 100, 2) as poor_query_percentage
from Queries
group by query_name