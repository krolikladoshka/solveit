-- https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/
with
    in_budget_candidates as
    (
        select
            c.experience,
            c.salary,
            sum(c.salary) over (
                partition by c.experience order by salary asc
            ) as boundary_salary
        from Candidates as c
    ),
    seniors as
    (
        select
            c.experience,
            max(c.boundary_salary) as max_salary,
            count(*) as accepted_candidates
        from in_budget_candidates as c
        where
            c.experience = 'Senior' and
            c.boundary_salary <= 70000
    ),
    juniors as
    (
        select
            c.experience,
            count(*) as accepted_candidates
            from in_budget_candidates as c
            where
                c.experience = 'Junior' and
                c.boundary_salary <= (
                    select 70000 - ifnull(s.max_salary, 0)
                    from seniors as s
                )
    )
select 'Senior' as experience, accepted_candidates
from seniors
union all
select 'Junior' as experience, accepted_candidates
from juniors