{{ config(
    materialized='incremental'
) }}


SELECT
    id,
    country,
    processed_time
FROM {{ source('user_activity', 'locations') }}
{% if is_incremental() %}
WHERE processed_time > (SELECT MAX(processed_time) FROM {{ this }})
{% endif %}