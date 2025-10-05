with cte as (
    select
        student_id,
        student_name,
        subject_name
    from
        Students
        cross join Subjects
)
select
    c.student_id,
    c.student_name,
    c.subject_name,
    count(e.student_id) as attended_exams
from
    cte c
    left join Examinations e on c.student_id = e.student_id
        and c.subject_name = e.subject_name
group by
    c.student_id,
    c.student_name,
    c.subject_name
order by
    student_id,
    subject_name