-- https://leetcode.com/problems/finding-the-topic-of-each-post/
select
    p.post_id,
    coalesce(
        group_concat(distinct k.topic_id),
        'Ambiguous!'
    ) as topic
from Posts as p
left join Keywords as k
on concat(' ', lower(p.content), ' ') like concat('% ', lower(k.word), ' %')
group by p.post_id