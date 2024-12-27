{{ config(
    materialized='ephemeral'
) }}

WITH joined_plays_with_dimensions AS (
    SELECT
        l.country AS country,
        t.licensor AS licensor,
        p.played_ms AS played_ms
    FROM {{ ref('stg_user_activity__plays') }} p
    INNER JOIN {{ ref('stg_user_activity__locations') }} l
        ON p.location_id = l.id
    INNER JOIN {{ ref('stg_user_activity__tracks') }} t
        ON p.track_id = t.id
)


SELECT
    country,
    licensor,
    COUNT(*) AS licensor_plays
FROM joined_plays_with_dimensions 
GROUP BY
    country,
    licensor