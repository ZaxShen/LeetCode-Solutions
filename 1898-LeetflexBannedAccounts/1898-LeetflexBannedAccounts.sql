-- Last updated: 8/4/2025, 10:44:05 PM
# Write your MySQL query statement below
select distinct l1.account_id
from LogInfo l1, LogInfo l2
where l1.account_id = l2.account_id
	and l1.login between l2.login and l2.logout
	and l1.ip_address != l2.ip_address;