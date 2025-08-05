-- Last updated: 8/4/2025, 10:45:32 PM
# Write your MySQL query statement below
select
    gender, day,
    sum(score_points) over(partition by gender order by day) as total
from Scores;