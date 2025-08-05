-- Last updated: 8/4/2025, 10:45:13 PM
# Write your MySQL query statement below
with cte(bin, total) as (
	select '[0-5>', sum(duration/60 < 5)
    from Sessions
    union
    select '[5-10>', sum(5 <= duration/60 and duration/60 < 10)
    from Sessions
    union
    select '[10-15>', sum(10 <= duration/60 and duration/60 < 15)
    from Sessions
    union
    select '15 or more', sum(15 <= duration/60)
    from Sessions
)
select * from cte;