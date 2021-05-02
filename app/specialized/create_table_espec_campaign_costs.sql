drop table if exists espec.campaign_costs;
create table espec.campaign_costs as
select dcm.campaign_name, sum(fcce.cost) as cost
from sot.fact_campaign_cost_effectiveness fcce
join sot.dim_campaign_media dcm on fcce.dim_campaign_media_id=dcm.dim_campaign_media_id
group by dcm.campaign_name
order by sum(fcce.cost) desc;