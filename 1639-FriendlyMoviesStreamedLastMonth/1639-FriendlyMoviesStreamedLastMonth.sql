-- Last updated: 8/4/2025, 10:44:30 PM
# Write your MySQL query statement below
select distinct(title) as title
from Content
inner join TVProgram using(content_id)
where year(program_date) = 2020
    and month(program_date) = 6
    and kids_content = 'Y'
    and content_type = 'Movies';