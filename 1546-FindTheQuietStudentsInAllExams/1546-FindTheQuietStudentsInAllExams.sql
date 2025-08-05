-- Last updated: 8/4/2025, 10:45:17 PM
/*SELECT the students who are in the middle of the rank of ALL exams
- Student PK: student_id
- Exam PK: (exam_id, student_id)

- SOLUTION: DENSE_RANK

- Step 1: Dense rank the students with ascending and descending for each exam
*/
WITH CTE AS
	(
    SELECT
		e.exam_id, e.student_id, s.student_name, e.score,
        DENSE_RANK() OVER(PARTITION BY exam_id ORDER BY score ASC) AS score_DR_ASC,
        DENSE_RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) AS score_DR_DESC
	FROM Exam e
    INNER JOIN Student s
		ON e.student_id = s.student_id
    )
#SELECT * FROM CTE;
# Step 2: Select the quiet student
SELECT DISTINCT student_id, student_name
FROM CTE
WHERE student_id NOT IN (SELECT student_id FROM CTE WHERE score_DR_ASC = 1 OR score_DR_DESC = 1)
ORDER BY student_id;