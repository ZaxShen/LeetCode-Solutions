-- Last updated: 8/4/2025, 10:44:23 PM
# Write your MySQL query statement below
select customer_id, count(visit_id) as count_no_trans
from Visits v
where visit_id not in (select visit_id from Transactions)
group by customer_id