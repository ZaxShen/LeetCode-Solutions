-- Last updated: 8/4/2025, 10:45:22 PM
select
    stock_name,
    sum(if(operation = 'Buy', -price, price)) as capital_gain_loss
from Stocks
group by stock_name
order by 2 desc;