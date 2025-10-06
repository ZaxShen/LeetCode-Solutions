WITH RECURSIVE
    cte (task_id, subtask_id) AS (
        SELECT task_id, 1
        FROM Tasks
        UNION
        SELECT
            c.task_id,
            c.subtask_id + 1
        FROM
            cte c
            JOIN Tasks t USING (task_id)
        WHERE c.subtask_id < t.subtasks_count
    )
SELECT
    c.task_id,
    c.subtask_id
FROM
    cte c
    LEFT JOIN Executed e ON c.task_id = e.task_id
    AND c.subtask_id = e.subtask_id
WHERE e.subtask_id IS NULL
ORDER BY task_id