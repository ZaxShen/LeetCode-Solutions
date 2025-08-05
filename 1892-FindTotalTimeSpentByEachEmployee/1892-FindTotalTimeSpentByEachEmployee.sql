-- Last updated: 8/4/2025, 10:44:04 PM
# Write your MySQL query statement below
SELECT
	event_day AS day,
	emp_id,
    SUM(out_time - in_time) AS total_time
FROM
	Employees
GROUP BY
	day,
    emp_id;