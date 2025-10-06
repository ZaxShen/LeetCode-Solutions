select distinct title
from
    TVProgram t
    join Content c using(content_id)
where to_char(t.program_date, 'YYYY-MM') = '2020-06'
    and c.Kids_content = 'Y'
    and c.content_type = 'Movies'