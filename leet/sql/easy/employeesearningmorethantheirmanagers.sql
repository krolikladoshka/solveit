select
    e.name as Employee
from
    Employee as e inner join Employee as m
    on e.managerId = m.id
where e.salary > m.salary
order by e.salary desc
``