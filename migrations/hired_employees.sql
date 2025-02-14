CREATE OR REPLACE TABLE `glbt-challenge-migrations.bq_glbt_migrator_tgt.ft_hired_employees` (
    ID INT64 OPTIONS (description = 'Id of the employee'),
    NAME STRING OPTIONS (description = 'Name of the employee'),
    DATETIME TIMESTAMP OPTIONS (description = 'Hire datetime in ISO format'),
    DEPARTMENT_ID INT64 OPTIONS (description = 'Id of the department which the employee was hired for'),
    JOB_ID INT64 OPTIONS (description = 'Id of the job which the employee was hired for'),
)
PARTITION BY DATE_TRUNC(DATETIME, DAY)  
CLUSTER BY NAME
OPTIONS (
    description = 'Table with the record of hired employees'
);

LOAD DATA OVERWRITE `glbt-challenge-migrations.bq_glbt_migrator_tgt.ft_hired_employees`
(ID INT64, NAME STRING, DATETIME TIMESTAMP, DEPARTMENT_ID INT64, JOB_ID INT64)
PARTITION BY DATE_TRUNC(DATETIME, DAY)  
CLUSTER BY NAME
FROM FILES (
  format = 'CSV',
  field_delimiter = ',',
  skip_leading_rows = 0,
  uris = ['gs://bq-glbt-migrator-6g/historic/hired_employees.csv']);