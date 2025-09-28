CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    with salary_rank as (
        select distinct
            e.salary,
            dense_rank() over(order by e.salary desc) as salary_desc
        from Employee e
    )
    select sr.salary
    from salary_rank sr
    where sr.salary_desc = N
  );
END;
$$ LANGUAGE plpgsql;