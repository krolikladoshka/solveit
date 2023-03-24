-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

select
    e.name
from Employee as e
left join Employee as m
on e.id = m.managerId
group by e.name
having count(e.id) >= 5
