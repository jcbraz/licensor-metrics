{{ config(
    materialized='incremental'
) }}


SELECT
    location_id,
    track_id,
    played_ms,
    processed_time
FROM {{ source('user_activity', 'plays') }}
{% if is_incremental() %}
WHERE processed_time > (SELECT MAX(processed_time) FROM {{ this }})
{% endif %}