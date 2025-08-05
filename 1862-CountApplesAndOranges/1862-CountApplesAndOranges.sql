-- Last updated: 8/4/2025, 10:44:07 PM
select
    sum(b.apple_count) + sum(ifnull(c.apple_count, 0)) as apple_count,
    sum(b.orange_count) + sum(ifnull(c.orange_count, 0)) as orange_count
from Boxes b
left join Chests c using(chest_id);