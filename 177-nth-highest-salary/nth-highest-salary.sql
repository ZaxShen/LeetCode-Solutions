CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    WITH salary_rank AS (
        SELECT DISTINCT
            e.salary,
            DENSE_RANK() OVER(ORDER BY e.salary DESC) AS salary_desc
        FROM Employee e
    )
    SELECT sr.salary
    FROM salary_rank sr
    WHERE sr.salary_desc = N
    -- LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;