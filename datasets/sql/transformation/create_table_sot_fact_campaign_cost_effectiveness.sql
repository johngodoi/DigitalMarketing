drop table if exists sot.fact_campaign_cost_effectiveness;
create table sot.fact_campaign_cost_effectiveness as
select
       dcm.dim_campaign_media_id
     , gamc.impressions
     , gamc.clicks
     , gamc.cost
     , gamc.date
from sor.google_ads_media_costs gamc
join sot.dim_campaign_media dcm
    on gamc.campaign_id=dcm.campaign_id
    and gamc.ad_creative_id=dcm.ad_creative_id
    and dcm.media='google'
union all
select
    dcm.dim_campaign_media_id
     , famc.impression
     , famc.clicks
     , famc.cost
     , famc.date
from sor.facebook_ads_media_costs famc
join sot.dim_campaign_media dcm
    on famc.campaign_id=dcm.campaign_id
    and dcm.media='facebook';