WITH cte AS (
    SELECT
        project_id,
        p.employee_id,
        DENSE_RANK() OVER (PARTITION BY p.project_id ORDER BY e.experience_years DESC) AS exp_desc
    FROM
        Project p
        JOIN Employee e USING (employee_id)
)
SELECT
    project_id,
    employee_id
FROM cte
WHERE exp_desc = 1
ORDER BY
    project_id ASC,
    employee_id ASC