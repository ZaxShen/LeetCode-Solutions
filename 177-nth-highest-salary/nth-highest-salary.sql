CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    with cte as (
        select
            e.salary,
            dense_rank() over(order by e.salary desc) as salary_desc
        from Employee e
    )
    select distinct cte.salary
    from cte
    where cte.salary_desc = N
  );
END;
$$ LANGUAGE plpgsql;