with
    unbannedUsers as (
        select
            users_id,
            role
        from Users
        where banned = 'No'
    ),
    Trips as (
        select
            *
        from Trips
        where request_at >= '2013-10-01' and request_at <= '2013-10-03'
    )
select
    t.request_at as Day,
    round(
        count(
            case
                when t.status in ('cancelled_by_driver', 'cancelled_by_client')
                then 1
            end
        )
        /
        count(t.status),
        2
     ) as "Cancellation Rate"
from Trips as t
inner join unbannedUsers as uu
on t.client_id = uu.users_id
inner join unbannedUsers as ud
on t.driver_id = ud.users_id
group by t.request_at