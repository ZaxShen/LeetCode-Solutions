-- Last updated: 8/4/2025, 10:45:14 PM
# Write your MySQL query statement below
select q.id, q.`year`, ifnull(npv, 0) as npv
from Queries q
left join NPV n on q.id = n.id and q.year = n.year
order by 1, 2;