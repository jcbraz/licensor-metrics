{{ config(
    materialized='table',
    enabled=true
) }}

WITH total_played_time AS (
    SELECT
        l.country,
        t.licensor,
        t.id AS track_id,
        SUM(p.played_ms) AS total_played_time,
        ROW_NUMBER() OVER (
            PARTITION BY l.country, t.licensor 
            ORDER BY SUM(p.played_ms) DESC
        ) AS rank
    FROM {{ ref('stg_user_activity__plays') }} p
    INNER JOIN {{ ref('stg_user_activity__tracks') }} t
        ON p.track_id = t.id
    INNER JOIN {{ ref('stg_user_activity__locations') }} l
        ON p.location_id = l.id
    GROUP BY l.country, t.licensor, t.id
)
SELECT 
    country,
    licensor,
    track_id,
    total_played_time
FROM total_played_time 
WHERE rank = 1