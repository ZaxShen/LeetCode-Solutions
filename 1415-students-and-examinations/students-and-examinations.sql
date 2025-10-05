with cte as (
    select distinct
        st.student_id,
        st.student_name,
        su.subject_name
    from
        Students st
        cross join Subjects su
)
select
    c.*,
    count(e.subject_name) as attended_exams
from
    cte c
    left join Examinations e on c.student_id = e.student_id
        and c.subject_name = e.subject_name
group by
    c.student_id,
    c.student_name,
    c.subject_name
order by student_id, subject_name