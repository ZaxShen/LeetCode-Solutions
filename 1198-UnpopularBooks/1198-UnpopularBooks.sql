-- Last updated: 8/5/2025, 12:20:06 AM
# Write your MySQL query statement below
with cte as
	(
	select 
		book_id, 
		`name`, 
        # Last 365 days from today
		if(dispatch_date between '2019-06-23' - interval 1 year and '2019-06-23', quantity, 0) as quanity_2018
        # Last calendar year
		#if(year(dispatch_date) = year('2019-06-23' - interval 1 year), quantity, 0) as quanity_2018
	from Books
	left join Orders using(book_id)
	where available_from < '2019-06-23' - interval 1 month
    )
select book_id, `name`
from cte
group by 1, 2
having sum(quanity_2018) < 10;