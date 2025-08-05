-- Last updated: 8/4/2025, 10:45:41 PM
# Write your MySQL query statement below
SELECT
    DISTINCT sub_id AS post_id,
    (SELECT COUNT(DISTINCT sub_id) FROM Submissions s2 WHERE s1.sub_id = s2.parent_id) AS number_of_comments
FROM
    Submissions AS s1
WHERE parent_id IS NULL
ORDER BY sub_id;