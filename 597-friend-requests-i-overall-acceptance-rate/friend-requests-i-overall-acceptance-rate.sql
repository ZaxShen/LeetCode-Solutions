select
    ROUND(COALESCE((select count(distinct (requester_id, accepter_id)) from RequestAccepted)::NUMERIC
    /
    NULLIF((select count(distinct (sender_id, send_to_id)) from FriendRequest), 0), 0), 2) as accept_rate
