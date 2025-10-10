select
    b.book_id,
    b.name
from
    Books b
    left join Orders o on b.book_id = o.book_id
    and o.dispatch_date between '2018-06-23'::DATE and '2019-06-23'::DATE
where
    b.available_from + interval '1 month' < '2019-06-23'::DATE
group by b.book_id, b.name
    having coalesce(sum(o.quantity), 0) < 10