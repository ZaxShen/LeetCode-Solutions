-- Last updated: 8/4/2025, 10:43:40 PM
# Write your MySQL query statement below
with cte as
	(
	select
		bus_id,
		arrival_time,
		ifnull(lag(arrival_time) over(), 0) as previous_time
	from (select * from Buses order by 2) b
	)
select 
	bus_id,
    count(passenger_id) as passengers_cnt
from cte
left join Passengers p
on p.arrival_time <= cte.arrival_time
and p.arrival_time > cte.previous_time
group by 1
order by 1;
