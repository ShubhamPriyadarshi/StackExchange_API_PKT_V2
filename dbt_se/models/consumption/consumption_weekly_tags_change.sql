{{ config(materialized='view', schema='consumption',tags='consumption', alias='weekly_tags_change') }}

select *
from {{ ref('calculation_weekly_tags_change') }}