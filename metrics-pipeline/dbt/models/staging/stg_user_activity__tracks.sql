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
    id,
    licensor,
    processed_time
FROM {{ source('user_activity', 'track') }}
{% if is_incremental() %}
WHERE processed_time > (SELECT max_time FROM last_processed)
{% endif %}