WITH all_friends AS (
    -- Get all friends of user 1 (bidirectional)
    SELECT user2_id AS friend_id
    FROM Friendship
    WHERE user1_id = 1
    
    UNION
    
    SELECT user1_id AS friend_id
    FROM Friendship
    WHERE user2_id = 1
)
SELECT DISTINCT l.page_id AS recommended_page
FROM all_friends f
JOIN Likes l ON f.friend_id = l.user_id
WHERE l.page_id NOT IN (
    SELECT page_id
    FROM Likes
    WHERE user_id = 1
)