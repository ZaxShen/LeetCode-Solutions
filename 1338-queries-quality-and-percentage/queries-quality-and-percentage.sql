select
    query_name,
    round(avg(rating::NUMERIC / position), 2) as quality,
    round(avg((rating < 3)::INT) * 100, 2) as poor_query_percentage
from Queries
group by query_name