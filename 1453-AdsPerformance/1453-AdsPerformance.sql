-- Last updated: 8/4/2025, 10:45:31 PM
# Write your MySQL query statement below
select 
	ad_id,
	ifnull(
		round(
		sum(if(action = 'Clicked', 1, 0)) 
		/
		sum(if(action = 'Clicked' or action = 'Viewed', 1, 0))
        * 100
		, 2)
	, 0) as ctr
from Ads
group by ad_id
order by 2 desc, 1 asc;