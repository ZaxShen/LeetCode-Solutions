select
    patient_id,
    patient_name,
    conditions
from Patients
where conditions ~ '(^|[*[:space:]])DIAB1'