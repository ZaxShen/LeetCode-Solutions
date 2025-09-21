SELECT
    request_at AS "Day",
    ROUND(
        COUNT(*) FILTER (WHERE status ILIKE 'cancelled%')::DECIMAL / COUNT(*),
        2
    ) AS "Cancellation Rate"
FROM
    trips t
    JOIN users client ON t.client_id = client.users_id 
        AND client.role = 'client' 
        AND client.banned = 'No'
    JOIN users driver ON t.driver_id = driver.users_id 
        AND driver.role = 'driver' 
        AND driver.banned = 'No'
WHERE request_at::DATE BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at
ORDER BY request_at;