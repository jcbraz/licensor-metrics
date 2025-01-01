{{ config(
    materialized='incremental'
) }}

SELECT
    id,
    licensor,
    processed_time
FROM {{ source('user_activity', 'tracks') }}
{% if is_incremental() %}
WHERE processed_time > (SELECT MAX(processed_time) FROM {{ this }})
{% endif %}