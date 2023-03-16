select
    sub.departmentName as Department,
    sub.name as Employee,
    sub.salary as Salary
from (
    select
        e.name,
        e.salary,
        d.name as departmentName,
        (dense_rank() over (partition by d.name order by d.name, e.salary desc)) as salaryRank
    from Employee as e
    inner join Department as d
    on e.departmentId = d.id
) as sub
where sub.salaryRank < 4