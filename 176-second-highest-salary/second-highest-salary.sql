WITH
    salary_rank AS (
        SELECT
            DISTINCT salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_desc
        FROM employee
    )
SELECT (SELECT salary
FROM salary_rank
WHERE salary_desc = 2) AS SecondHighestSalary