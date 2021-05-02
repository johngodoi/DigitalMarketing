drop table if exists sot.dim_viewer;
create table sot.dim_viewer as
select
    row_number() over (order by device_id)
           as dim_viewer_id
       , *
from (
         select trim(device_id) as device_id
         from sor.pageviews
         group by device_id
     )t;