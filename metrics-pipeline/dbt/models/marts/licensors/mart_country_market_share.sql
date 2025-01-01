{{ config(
    materialized='table',
    enabled=true,
    cache={
        'enabled': true
    }
) }}
SELECT
    lc.country AS country,
    lc.licensor AS licensor,
    ROUND(COALESCE(CAST(lc.licensor_plays AS NUMERIC) / 
           NULLIF(CAST(tc.total_country_plays AS NUMERIC), 0), 0), 4) AS market_share
FROM {{ ref('int_licensor_plays_per_country_count') }} lc
INNER JOIN {{ ref('int_total_plays_per_country_count') }} tc
    ON lc.country = tc.country
ORDER BY
    lc.country,
    market_share DESC