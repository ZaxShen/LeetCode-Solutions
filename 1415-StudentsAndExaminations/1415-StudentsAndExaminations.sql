-- Last updated: 8/4/2025, 10:45:37 PM
# Write your MySQL query statement below
select s.student_id, s.student_name, sub.subject_name, count(e.subject_name) as attended_exams
from Students s
inner join Subjects sub
left join Examinations e
    on s.student_id = e.student_id and sub.subject_name = e.subject_name
group by 1, 2, 3
order by 1, 3