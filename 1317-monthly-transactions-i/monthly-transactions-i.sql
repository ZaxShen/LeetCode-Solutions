SELECT
    TO_CHAR(trans_date, 'YYYY-MM') AS MONTH,
    country,
    COUNT(*) AS trans_count,
    COUNT(*) FILTER (WHERE "state" = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN "state" = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY MONTH, country
ORDER BY MONTH, country