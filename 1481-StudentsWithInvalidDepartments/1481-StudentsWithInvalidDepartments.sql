-- Last updated: 8/4/2025, 10:45:28 PM
# Write your MySQL query statement below
SELECT id, name
FROM Students
WHERE department_id NOT IN (SELECT id FROM Departments);