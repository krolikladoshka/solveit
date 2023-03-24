--https://leetcode.com/problems/department-highest-salary/

select
    sub.Department as Department,
    sub.Employee as Employee,
    sub.Salary as Salary
from (
    select
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        rank() over (
            partition by d.name
            order by e.salary desc
        ) as salary_rank
    from Employee as e
    inner join Department as d
    on e.departmentId = d.id
) as sub
where salary_rank = 1
