select coalesce(
    round(
        (select count(distinct (requester_id, accepter_id))::numeric
        from RequestAccepted)
        /
        (select nullif(count(distinct (sender_id, send_to_id)), 0)
        from FriendRequest),
        2), 
    0)  as accept_rate