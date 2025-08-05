-- Last updated: 8/4/2025, 10:45:34 PM
# Write your MySQL query statement below
select
    country_name,
    case
        when avg(weather_state) <= 15 then 'Cold'
        when avg(weather_state) >= 25 then 'Hot'
        else 'Warm'
    end as weather_type
from Countries
left join Weather using(country_id)
where date_format(day, '%Y-%m') = '2019-11'
group by 1;