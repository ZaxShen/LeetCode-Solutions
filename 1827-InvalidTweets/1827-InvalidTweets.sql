-- Last updated: 8/4/2025, 10:44:11 PM
# Write your MySQL query statement below
select tweet_id
from Tweets
where length(content) > 15