CREATE OR REPLACE TABLE `glbt-challenge-migrations.bq_glbt_migrator_tgt.dm_jobs` (
    ID INT64 OPTIONS (description = 'Job ID'),
    JOB STRING OPTIONS (description = 'Job name')
) 
CLUSTER BY JOB
OPTIONS (
    description = 'Table with the list of jobs'
);

LOAD DATA OVERWRITE `glbt-challenge-migrations.bq_glbt_migrator_tgt.dm_jobs`
(ID INT64, JOB STRING)
CLUSTER BY JOB
FROM FILES (
  format = 'CSV',
  field_delimiter = ',',
  skip_leading_rows = 0,
  uris = ['gs://bq-glbt-migrator-6g/historic/jobs.csv']);