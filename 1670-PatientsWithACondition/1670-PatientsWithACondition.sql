-- Last updated: 8/4/2025, 10:44:26 PM
SELECT
    patient_id,
    patient_name,
    conditions
FROM Patients
WHERE conditions LIKE "DIAB1%"
    OR conditions LIKE "% DIAB1%"