-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times

select
    ad.actor_id,
    ad.director_id
from ActorDirector as ad
group by ad.actor_id, ad.director_id
having count(director_id) >= 3
