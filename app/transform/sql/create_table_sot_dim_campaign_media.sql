drop table if exists sot.dim_campaign_media;
create table sot.dim_campaign_media as
select
       row_number() over (order by media, campaign_id, ad_creative_id)
           as dim_campaign_media_id
       , *
from (
         select campaign_id
              , campaign_name
              , ad_creative_id
              , ad_creative_name
              , 'google' as media
         from sor.google_ads_media_costs
         group by campaign_id, campaign_name, ad_creative_id, ad_creative_name
         union all
         select campaign_id
              , campaign_name
              , null       as ad_creative_id
              , ''         as ad_creative_name
              , 'facebook' as media
         from sor.facebook_ads_media_costs
         group by campaign_id, campaign_name
         order by media, campaign_id, campaign_name, ad_creative_id, ad_creative_name
     ) t;