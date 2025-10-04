SELECT DISTINCT
    l1.account_id
FROM
    LogInfo l1
    JOIN LogInfo l2 ON l1.account_id = l2.account_id
    AND l1.ip_address != l2.ip_address
WHERE
    l1.login <= l2.logout
    AND l1.logout >= l2.login;