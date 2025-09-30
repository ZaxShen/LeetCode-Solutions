WITH cumulative_costs AS (
    SELECT
        employee_id,
        experience,
        salary,
        SUM(salary) OVER(
            PARTITION BY experience 
            ORDER BY salary ASC, employee_id ASC
        ) AS running_total
    FROM Candidates
),
seniors_hired AS (
    SELECT 
        COUNT(*) AS senior_count,
        COALESCE(MAX(running_total), 0) AS senior_spent
    FROM cumulative_costs
    WHERE experience = 'Senior' 
        AND running_total <= 70000
)
SELECT 
    'Senior' AS experience,
    senior_count AS accepted_candidates
FROM seniors_hired
UNION ALL
SELECT 
    'Junior' AS experience,
    COUNT(*) AS accepted_candidates
FROM cumulative_costs
CROSS JOIN seniors_hired
WHERE experience = 'Junior'
    AND running_total <= 70000 - senior_spent;