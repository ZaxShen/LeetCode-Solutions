-- Last updated: 8/4/2025, 10:43:46 PM
# Write your MySQL query statement below
select school_id, ifnull(min(score), -1) as score
from Schools
left join Exam on capacity >= student_count
group by 1;