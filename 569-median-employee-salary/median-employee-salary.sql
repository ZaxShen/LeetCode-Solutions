WITH ranked AS (
    SELECT 
        id,
        company,
        salary,
        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary) AS rn,
        COUNT(*) OVER (PARTITION BY company) AS cnt
    FROM Employee
)
SELECT 
    id,
    company,
    salary
FROM ranked
WHERE rn BETWEEN cnt / 2.0 AND cnt / 2.0 + 1
ORDER BY company, salary;