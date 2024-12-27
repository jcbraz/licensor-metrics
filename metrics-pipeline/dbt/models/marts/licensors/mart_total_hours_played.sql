{{ config(
    materialized='table',
    enabled=true,
    cache={
        'enabled': true
    }
) }}


SELECT
  t.licensor AS licensor,
  ROUND(SUM(p.played_ms) / 3600000, 0) AS total_hours_played
FROM {{ ref('stg_user_activity__tracks') }} t
INNER JOIN {{ ref('stg_user_activity__plays') }} p
  ON t.id = p.track_id
GROUP BY t.licensor