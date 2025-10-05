select
    -- viewer_id,
    -- view_date,
    -- count(distinct article_id) as views
    distinct viewer_id as id
from Views
group by viewer_id, view_date
    having count(distinct article_id) >= 2