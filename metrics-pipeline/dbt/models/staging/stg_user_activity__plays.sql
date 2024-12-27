{{ config(
    materialized='incremental'
) }}

{% if is_incremental() %}
WITH last_processed AS (
    SELECT MAX(processed_time) as max_time 
    FROM {{ this }}
)
{% endif %}

SELECT
    locationid AS location_id,
    trackid AS track_id,
    playedMs AS played_ms,
    processed_time
FROM {{ source('user_activity', 'play') }}
{% if is_incremental() %}
WHERE processed_time > (SELECT max_time FROM last_processed)
{% endif %}