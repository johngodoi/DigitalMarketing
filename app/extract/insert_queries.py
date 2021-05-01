insert_queries = {
    "facebook": "INSERT INTO sor.facebook_ads_media_costs (clicks, cost, date, campaign_id, campaign_name, impression) VALUES {}",
    "google": "INSERT INTO sor.google_ads_media_costs (ad_creative_id, ad_creative_name, clicks, cost, date, campaign_id, campaign_name, impressions) VALUES {}",
    "customer_leads": "INSERT INTO sor.customer_leads (device_id, lead_id, registered_at, credit_decision, credit_decision_at, signed_at, revenue) VALUES {}",
    "pageviews": "INSERT INTO sor.pageviews (ip_address, datetime, url, campaign_id, ad_creative_id, device_id, referer) VALUES {}"
}
