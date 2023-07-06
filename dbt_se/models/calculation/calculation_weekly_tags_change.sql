{{ config(materialized='table', schema='calculation',tags='calculation', alias='weekly_tags_change') }}

SELECT
    tag_name,
    MAX(daily_tag_count) - MIN(daily_tag_count) as weekly_change
FROM
    (
        SELECT
            load_date,
            tag_name,
            SUM(daily_count) OVER (PARTITION BY load_date, tag_name) as daily_tag_count
        FROM
            {{ ref('calculation_daily_tags') }}
        WHERE
            load_date BETWEEN CURRENT_DATE - INTERVAL '7 day' AND CURRENT_DATE
    ) as subquery
GROUP BY
    tag_name
ORDER BY
    weekly_change DESC
