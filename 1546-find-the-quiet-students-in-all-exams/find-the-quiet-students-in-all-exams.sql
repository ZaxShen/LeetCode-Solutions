with cte as (
    select
        s.student_id,
        s.student_name,
        e.exam_id,
        dense_rank() over(partition by e.exam_id order by e.score asc) as score_asc,
        dense_rank() over(partition by e.exam_id order by e.score desc) as score_desc
    from Student s
    join Exam e using(student_id)
)
select distinct
    student_id,
    student_name
from cte s
where not exists (
    select student_id
    from cte
    where s.student_id = cte.student_id
        and (score_asc = 1 or score_desc = 1)
)
order by s.student_id asc