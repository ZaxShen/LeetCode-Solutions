  SELECT
      contest_id,
      ROUND(
          COUNT(*)::DECIMAL / (
              SELECT COUNT(*) FROM Users
          ) * 100,
          2
      ) AS percentage
  FROM
      register
  GROUP BY
      contest_id
  ORDER BY
      percentage DESC,
      contest_id ASC