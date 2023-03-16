delete a from
    Person as a
    left join Person as b
    on a.email = b.email
where a.id > b.id
