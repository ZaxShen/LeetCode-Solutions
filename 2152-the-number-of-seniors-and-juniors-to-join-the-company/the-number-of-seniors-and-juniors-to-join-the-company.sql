WITH
    cte AS (
        SELECT
            *,
            SUM(salary) OVER (PARTITION BY experience ORDER BY salary ASC, employee_id ASC) AS total_salary
        FROM Candidates
    ),
    hired_seniors AS (
        SELECT COALESCE(total_salary, 0) AS total_salary
        FROM cte
        WHERE
            experience = 'Senior'
            AND total_salary <= 70000
    )
SELECT
    'Senior' AS experience,
    COUNT(*) AS accepted_candidates
FROM hired_seniors
UNION ALL
SELECT
    'Junior' AS experience,
    COUNT(*) AS accepted_candidates
FROM cte
WHERE
    experience = 'Junior'
    AND total_salary <= 70000 - (SELECT COALESCE(MAX(total_salary), 0) FROM hired_seniors)