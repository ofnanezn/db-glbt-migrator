MERGE INTO bq_glbt_migrator_tgt.ft_hired_employees tgt
USING bq_glbt_migrator_stg.<staging_table> stg
ON tgt.id = stg.id
WHEN MATCHED THEN
  UPDATE SET
    tgt.name = stg.name
    tgt.datetime = stg.datetime
    tgt.department_id = stg.department_id
    tgt.job_id = stg.job_id
WHEN NOT MATCHED THEN
  INSERT VALUES (
    stg.id,
    stg.name,
    stg.datetime,
    stg.department_id,
    stg.job_id
  )
    