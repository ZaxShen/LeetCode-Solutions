select (
    select distinct salary as SecondHighestSalary
    from Employee
    order by salary desc
    offset 1
    limit 1
)