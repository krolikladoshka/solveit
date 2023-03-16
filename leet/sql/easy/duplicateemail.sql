select
    r.email
from (
    select
        p.id,
        p.email,
        (row_number() over (partition by p.email order by p.email)) as r
    from Person as p
) as r
where r.r = 2

