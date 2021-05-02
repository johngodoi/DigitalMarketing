drop table if exists sot.fact_credit_decision;
create table sot.fact_credit_decision as
select
    dcl.dim_customer_lead_id
     , cl.credit_decision
     , case when cl.credit_decision = 'A' then 'Aprovado'
            when cl.credit_decision = 'D' then 'Reprovado'
            else 'Sem avaliação' end as credit_decision_description
     , cl.credit_decision_at
from sor.customer_leads cl
join sot.dim_customer_lead dcl
    on cl.device_id=dcl.device_id and cl.lead_id = dcl.lead_id;