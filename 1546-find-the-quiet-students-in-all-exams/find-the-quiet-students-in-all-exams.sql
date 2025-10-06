with cte as (
    select
        s.student_id,
        s.student_name,
        dense_rank() over(partition by e.exam_id order by e.score asc) as socre_asc,
        dense_rank() over(partition by e.exam_id order by e.score desc) as socre_desc
    from
        Student s
        join Exam e on s.student_id = e.student_id
)
select distinct
    student_id,
    student_name
from cte
where student_id not in (
    select student_id from cte where socre_asc = 1 or socre_desc = 1
)
order by student_id