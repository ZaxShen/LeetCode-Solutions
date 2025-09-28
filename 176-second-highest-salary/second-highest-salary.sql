WITH
    salary_rank AS (
        SELECT
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_desc
        FROM employee
    )
SELECT MAX(salary) AS SecondHighestSalary
FROM salary_rank
WHERE salary_desc = 2