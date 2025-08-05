-- Last updated: 8/4/2025, 10:46:01 PM
# Write your MySQL query statement below
SELECT
	extra AS report_reason, 
    COUNT(DISTINCT post_id) AS report_count
FROM
	Actions
WHERE
	DATEDIFF('2019-07-05', action_date) = 1
    AND
    action = 'Report'
GROUP BY
	report_reason
;