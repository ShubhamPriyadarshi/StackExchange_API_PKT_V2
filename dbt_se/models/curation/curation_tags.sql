{{ config(materialized='table', schema='curation',tags='curation', alias='tags') }}

with base as (
  select
    cast(name as varchar) as tag_name,
    cast(count as number) as tag_count,
    cast(ingestion_timestamp as timestamp) as ingestion_timestamp
  from {{ source('ingestion', 'tags') }}
)

select
  tag_name,
  tag_count,
  ingestion_timestamp
from base
