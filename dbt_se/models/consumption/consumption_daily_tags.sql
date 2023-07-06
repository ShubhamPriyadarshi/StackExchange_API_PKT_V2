{{ config(materialized='view', schema='consumption',tags='consumption', alias='daily_tags') }}

select *
from {{ ref('calculation_daily_tags') }}