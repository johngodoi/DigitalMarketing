drop table if exists sot.fact_page_views;
create table sot.fact_page_views as
select
       dv.dim_viewer_id
     , dcm.dim_campaign_media_id
     , spv.url
     , spv.datetime
     , spv.referer
     , spv.ip_address
from sor.pageviews spv
join sot.dim_viewer dv on spv.device_id=dv.device_id
left join sot.dim_campaign_media dcm
    on spv.campaign_id=cast(dcm.campaign_id as varchar(20))
    and spv.ad_creative_id=cast(dcm.ad_creative_id as varchar(20))
    and spv.referer  like '%' || dcm.media || '%';