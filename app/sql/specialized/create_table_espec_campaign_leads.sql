drop table if exists espec.campaign_leads;
create table espec.campaign_leads as
select dcm.campaign_name, dcm.ad_creative_name, count(*) as leads
from sot.dim_customer_lead dcl
join sot.dim_viewer dv on dcl.device_id=dv.device_id
join sot.fact_page_views fpv on fpv.dim_viewer_id=dv.dim_viewer_id
    and fpv.dim_campaign_media_id is not null
join sot.dim_campaign_media dcm on fpv.dim_campaign_media_id=dcm.dim_campaign_media_id
group by dcm.campaign_name, dcm.ad_creative_name
order by leads desc;