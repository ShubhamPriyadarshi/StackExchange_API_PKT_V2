{{ config(materialized='table', schema='calculation',tags='calculation', alias='daily_tags') }}

with base as (
  select
    TO_DATE(date_trunc('day', ingestion_timestamp)) as load_date,
    tag_name,
    tag_count
  from {{ ref('curation_tags') }}
)

select
  load_date,
  tag_name,
  max(tag_count) as daily_count
from base
group by 1, 2
order by 1, 2
