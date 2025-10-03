SELECT
    ROUND(
        COALESCE(
            (SELECT COUNT(DISTINCT (requester_id, accepter_id)) FROM RequestAccepted)::NUMERIC 
            / 
            NULLIF(
             (SELECT COUNT(DISTINCT (sender_id, send_to_id)) FROM FriendRequest),
            0),
        0.00),
    2) AS accept_rate;