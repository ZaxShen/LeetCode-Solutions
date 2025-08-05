-- Last updated: 8/4/2025, 10:45:29 PM
(
select name as results
from MovieRating m
inner join Users using(user_id)
group by m.user_id
order by count(user_id) desc, name asc
limit 1
)
union all
(
select title as results
from MovieRating m
inner join Movies using(movie_id)
where extract(year_month from created_at) = 202002
group by m.movie_id
order by avg(rating) desc, title asc
limit 1
);