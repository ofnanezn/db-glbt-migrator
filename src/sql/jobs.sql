MERGE INTO bq_glbt_migrator_tgt.dm_jobs tgt
USING bq_glbt_migrator_stg.<staging_table> stg
ON tgt.id = stg.id
WHEN MATCHED THEN
  UPDATE SET
    tgt.job = stg.job
WHEN NOT MATCHED THEN
  INSERT VALUES (
    stg.id,
    stg.job
  )
    