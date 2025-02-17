DECLARE MEAN_2021 FLOAT64;
SET MEAN_2021 = (
  WITH HIRED_PER_DPT_2021 AS (
    SELECT
      DEPARTMENT_ID, 
      COUNT(*) HIRED
    FROM bq_glbt_migrator_tgt.ft_hired_employees
    WHERE EXTRACT(YEAR FROM DATETIME) = 2021
    GROUP BY 1
  )
  SELECT
    AVG(HIRED)
  FROM HIRED_PER_DPT_2021
);

SELECT 
  d.ID,
  d.DEPARTMENT,
  COUNT(*) HIRED, 
FROM bq_glbt_migrator_tgt.ft_hired_employees he
JOIN bq_glbt_migrator_tgt.dm_departments d 
  ON he.DEPARTMENT_ID = d.ID 
GROUP BY 1, 2
HAVING COUNT(*) > MEAN_2021
ORDER BY 3 DESC;