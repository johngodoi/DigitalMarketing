drop table if exists espec.campaign_clicks;
create table espec.campaign_clicks as
select dcm.campaign_name, sum(fcce.clicks) as clicks
from sot.fact_campaign_cost_effectiveness fcce
join sot.dim_campaign_media dcm on fcce.dim_campaign_media_id=dcm.dim_campaign_media_id
group by dcm.campaign_name
order by clicks desc;