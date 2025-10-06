with cte as (
    select
        *,
        dense_rank() over(partition by student_id order by grade desc, course_id asc) as grade_desc
    from Enrollments
)
select
    student_id,
    course_id,
    grade
from cte
where grade_desc = 1
order by student_id