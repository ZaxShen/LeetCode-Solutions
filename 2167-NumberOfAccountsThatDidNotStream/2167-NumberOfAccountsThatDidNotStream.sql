-- Last updated: 8/4/2025, 10:43:44 PM
# Write your MySQL query statement below
select count(*) accounts_count
from Subscriptions s1
inner join Streams s2 using(account_id)
where year(end_date) = 2021 and year(stream_date) != 2021;