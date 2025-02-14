MERGE INTO bq_glbt_migrator_tgt.dm_departments tgt
USING bq_glbt_migrator_stg.<staging_table> stg
ON tgt.id = stg.id
WHEN MATCHED THEN
  UPDATE SET
    tgt.department = stg.department
WHEN NOT MATCHED THEN
  INSERT VALUES (
    stg.id,
    stg.department
  )
    