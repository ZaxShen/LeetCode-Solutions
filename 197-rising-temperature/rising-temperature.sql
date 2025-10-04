select w2.id
from Weather w1
    join Weather w2 on w1.recordDate + 1 = w2.recordDate
where w1.temperature < w2.temperature