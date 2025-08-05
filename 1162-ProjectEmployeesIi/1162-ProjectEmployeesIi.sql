-- Last updated: 8/4/2025, 10:46:15 PM
# Write your MySQL query statement below

WITH CTE AS
    (
    SELECT
        project_id,
        DENSE_RANK() OVER(ORDER BY COUNT(employee_id) DESC) AS n_employee_DR
    FROM Project
    GROUP BY project_id
    )
SELECT project_id
FROM CTE
WHERE n_employee_DR = 1;