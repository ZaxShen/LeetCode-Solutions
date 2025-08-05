-- Last updated: 8/4/2025, 10:45:57 PM
# Write your MySQL query statement below
select distinct(viewer_id) as id
from Views
group by viewer_id, view_date
having count(distinct(article_id)) > 1;