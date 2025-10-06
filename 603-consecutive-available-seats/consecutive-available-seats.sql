WITH grouped_seats AS (
    SELECT
        seat_id,
        seat_id - ROW_NUMBER() OVER (ORDER BY seat_id) AS grp
    FROM Cinema
    WHERE free = 1
),
seat_counts AS (
    SELECT
        seat_id,
        grp,
        COUNT(*) OVER (PARTITION BY grp) AS group_size
    FROM grouped_seats
)
SELECT seat_id
FROM seat_counts
WHERE group_size >= 2
ORDER BY seat_id;