-- Last updated: 8/4/2025, 10:45:56 PM
# Write your MySQL query statement below
select distinct author_id as id
from Views
where author_id = viewer_id
order by id asc