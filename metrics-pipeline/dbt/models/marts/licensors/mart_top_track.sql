-- overall top performing track for a lincensor (measured in total played_ms)

{{ config(
    materialized='table',
    enabled=true,
    cache={
        'enabled': true
    }
) }}

WITH total_track_played_time AS (
  SELECT
    p.track_id AS track_id,
    SUM(p.played_ms) AS total_played_time
  FROM {{ ref('stg_user_activity__plays') }} p
  GROUP BY p.track_id
),
track_per_licensor_rank AS (
    SELECT
        stg_track.licensor AS licensor,
        tt.track_id AS track_id,
        tt.total_played_time AS total_played_time,
        DENSE_RANK() OVER (
            PARTITION BY stg_track.licensor
            ORDER BY tt.total_played_time DESC
        ) AS play_time_rank
    FROM total_track_played_time tt
    INNER JOIN {{ ref('stg_user_activity__tracks') }} stg_track
        ON tt.track_id = stg_track.id
)

SELECT
    *
FROM
    track_per_licensor_rank
WHERE play_time_rank = 1
    