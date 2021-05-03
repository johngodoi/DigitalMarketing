drop view if exists espec.campaign_efficiency;
create view espec.campaign_efficiency as
select
       sum(clicks) as clicks
     , sum(leads) as leads
     , sum(revenue) as revenue
     , sum(cost) as cost
     , sum(revenue)-sum(cost) as profit
     , campaign_name
     , ad_creative_name
from(
select 0 as clicks, 0 as leads, 0 as revenue, cost as cost, campaign_name, ad_creative_name
from espec.campaign_costs
union all
select 0 as clicks, 0 as leads, revenue as revenue, 0  as cost, campaign_name, ad_creative_name
from espec.campaign_revenue
union all
select 0 as clicks, leads as leads, 0 as revenue, 0  as cost, campaign_name, ad_creative_name
from espec.campaign_leads
union all
select clicks as clicks, 0 as leads, 0 as revenue, 0  as cost, campaign_name, ad_creative_name
from espec.campaign_clicks
) t
group by campaign_name, ad_creative_name