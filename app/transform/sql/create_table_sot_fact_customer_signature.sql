drop table if exists sot.fact_customer_signature;
create table sot.fact_customer_signature as
select
    dcl.dim_customer_lead_id
     , cl.signed_at
     , cast(cl.revenue as double precision)
from sor.customer_leads cl
join sot.dim_customer_lead dcl
              on cl.device_id=dcl.device_id and cl.lead_id = dcl.lead_id
where signed_at is not null;