-- Last updated: 8/4/2025, 10:45:12 PM
select e.left_operand, e.operator, e.right_operand,
	case
		when operator = '=' and v1.value = v2.value then 'true'
        when operator = '>' and v1.value > v2.value then 'true'
        when operator = '<' and v1.value < v2.value then 'true'
        else 'false'
	end as value
from Expressions e
left join Variables v1 on v1.name = e.left_operand
left join Variables v2 on v2.name = e.right_operand;