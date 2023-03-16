-- https://leetcode.com/problems/human-traffic-of-stadium
select
    sub.id,
    sub.visit_date,
    sub.people
from (
    select
        s.id,
        s.visit_date,
        s.people,
        lag(s.people, 2) over (
            order by s.visit_date asc
        ) as prev2,
        lag(s.people, 1) over (
            order by s.visit_date asc
        ) as prev,
        lead(s.people, 1) over (
            order by s.visit_date asc
        ) as next,
        lead(s.people, 2) over (
            order by s.visit_date asc
        ) as next2
    from Stadium as s
) as sub
where
    (
        sub.people >= 100 and
        sub.next >= 100 and
        sub.next2 >= 100
    ) or
    (
        sub.people >= 100 and
        sub.prev >= 100 and
        sub.next >= 100
    ) or
    (
        sub.prev2 >= 100 and
        sub.prev >= 100 and
        sub.people >= 100
    )