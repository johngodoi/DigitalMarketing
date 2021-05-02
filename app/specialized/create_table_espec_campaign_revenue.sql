drop table if exists espec.campaign_revenue;
create table espec.campaign_revenue as
select dcm.campaign_name, dcm.ad_creative_name, sum(fcs.revenue) as revenue
from sot.fact_customer_signature fcs
join sot.dim_customer_lead dcl on fcs.dim_customer_lead_id=dcl.dim_customer_lead_id
join sot.dim_viewer dv on dcl.device_id=dv.device_id
join sot.fact_page_views fpv on fpv.dim_viewer_id=dv.dim_viewer_id
    and fpv.dim_campaign_media_id is not null
 join sot.dim_campaign_media dcm on fpv.dim_campaign_media_id=dcm.dim_campaign_media_id
group by dcm.campaign_name, dcm.ad_creative_name
order by revenue desc;