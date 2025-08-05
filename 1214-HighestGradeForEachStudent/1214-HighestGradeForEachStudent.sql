-- Last updated: 8/4/2025, 10:46:04 PM
with cte as
    (
    select
        student_id,
        course_id,
        grade,
        rank() over(partition by student_id order by grade desc, course_id asc) as dr_grade
    from Enrollments
    )
select student_id, course_id, grade
from cte
where dr_grade = 1
order by 1;