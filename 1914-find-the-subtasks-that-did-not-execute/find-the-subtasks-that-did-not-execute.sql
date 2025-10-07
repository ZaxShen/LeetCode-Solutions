select
    t.task_id,
    s.subtask_id
from
    Tasks t
    cross join generate_series(1, subtasks_count) as s(subtask_id)
    left join Executed e on t.task_id = e.task_id
        and s.subtask_id = e.subtask_id
where e.subtask_id is NULL