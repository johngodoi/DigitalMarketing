drop table if exists sot.dim_customer_lead;
create table sot.dim_customer_lead as
select
    row_number() over (order by device_id, lead_id, registered_at)
           as dim_customer_lead_id
       , *
from (
         select trim(device_id) as device_id
              , lead_id
              , registered_at
         from sor.customer_leads
         group by device_id, lead_id, registered_at
     )t;