-- https://leetcode.com/problems/big-countries
select
    w.name,
    w.population,
    w.area
from World as w
where w.population >= 25000000 or w.area >= 3000000
