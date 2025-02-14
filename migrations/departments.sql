CREATE OR REPLACE TABLE `glbt-challenge-migrations.bq_glbt_migrator_tgt.dm_departments` (
    ID INT64 OPTIONS (description = 'Department ID'),
    DEPARTMENT STRING OPTIONS (description = 'Department name')
) 
CLUSTER BY DEPARTMENT
OPTIONS (
    description = 'Table with the list of departments'
);

LOAD DATA OVERWRITE `glbt-challenge-migrations.bq_glbt_migrator_tgt.dm_departments`
(ID INT64, DEPARTMENT STRING)
CLUSTER BY DEPARTMENT
FROM FILES (
  format = 'CSV',
  field_delimiter = ',',
  skip_leading_rows = 0,
  uris = ['gs://bq-glbt-migrator-6g/historic/departments.csv']);