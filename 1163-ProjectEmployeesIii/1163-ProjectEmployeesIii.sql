-- Last updated: 8/4/2025, 10:46:15 PM
/*Query the the most experienced employees in each project
Project PK: (project_id, employee_id)
Employee PK: employee_id
*/
WITH CTE AS
    (
    SELECT 
        p.project_id,
        p.employee_id,
        DENSE_RANK() OVER(PARTITION BY p.project_id ORDER BY e.experience_years DESC) AS experience_DR
    FROM Project p
    INNER JOIN Employee e
        USING(employee_id)
    )
SELECT project_id, employee_id
FROM CTE
WHERE experience_DR = 1;