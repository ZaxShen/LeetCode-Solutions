select
    patient_id,
    patient_name,
    conditions
from Patients
where conditions ~ '(^|[\ ])DIAB1'