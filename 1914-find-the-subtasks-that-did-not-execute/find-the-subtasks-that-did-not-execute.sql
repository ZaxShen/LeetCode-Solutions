with recursive cte(task_id, subtask_id) as (
    select
        task_id,
        1
    from Tasks
    union all
    select
        c.task_id,
        c.subtask_id + 1
    from cte c
    join Tasks t using(task_id)
    where c.subtask_id < t.subtasks_count
)
select
    c.task_id,
    c.subtask_id
from
    cte c
    left join Executed e on c.task_id = e.task_id
        and c.subtask_id = e.subtask_id
where e.subtask_id is NULL
order by task_id
