-- rank stduents
-- find students with at least one exma
-- output result and order by student_id

with student_rank as (
    select
        e.exam_id,
        e.student_id,
        s.student_name,
        dense_rank() over(partition by e.exam_id order by e.score asc) as score_asc,
        dense_rank() over(partition by e.exam_id order by e.score desc) as score_desc
    from Exam e
    left join Student s using(student_id)
)
select distinct
    student_id,
    student_name
from student_rank
where student_id not in (
    select student_id
    from student_rank 
    where score_asc = 1
        or score_desc = 1
)
order by student_id