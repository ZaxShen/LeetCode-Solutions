-- Last updated: 8/4/2025, 10:43:30 PM
# Write your MySQL query statement below
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id