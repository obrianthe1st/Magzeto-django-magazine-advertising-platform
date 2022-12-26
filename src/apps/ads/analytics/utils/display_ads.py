from apps.ads.advert.models import SearchAd, SponsoredAd
from apps.ads.campaign.models import SearchCampaign, SponsoredCampaign


#A class that stores the campaigns that will be used at a time
class Campaign_Queue:

    def __init__(self):
        self.queue = []

    def add_campaign(self,campaign):
        self.queue.append(campaign)

class Ad_Queue():

    def __init__(self):
        self.queue = []

    def add_campaign(self,ad):
        self.queue.append(ad)



def homePageSponsoredAds():
    campaigns = SponsoredCampaign.objects.all()
    campaign_queue = Campaign_Queue()

    if campaigns.count() > 1:
        for each_campaign in campaigns[:2]:
            campaign_queue.add_campaign(each_campaign)
    elif campaigns.count() == 0:
        return None
    else:
        campaign_queue.add_campaign(campaigns)
    
    ads_queue = Ad_Queue()
    if len(campaign_queue.queue) > 1:
        for campaign in campaign_queue.queue:
            sponsoredads = SponsoredAd.objects.filter(campaign_id=campaign.id)
            for each_ad in sponsoredads:
                ads_queue.queue.append(each_ad)
    else:
         for campaign in campaign_queue.queue:
            sponsoredads = SponsoredAd.objects.filter(campaign_id=campaign[0].id)
            for each_ad in sponsoredads:
                ads_queue.queue.append(each_ad)


    return ads_queue.queue



def searchPageAds():
    campaigns = SearchCampaign.objects.all()

    campaign_queue = Campaign_Queue()
    

    #get the campaigns
    # I think I might need a campaign handler class in the future to rotate the campaigns, this will
     #ensure that each set of campaigns get a particular time spent on the list
    if campaigns.count() > 1:
        for each_campaign in campaigns[:2]:
            campaign_queue.add_campaign(each_campaign)
    elif campaigns.count() == 0:
        return None
    else:
        campaign_queue.add_campaign(campaigns)

    #get the ads from each campaign
    
    ads_queue = Ad_Queue()
    if len(campaign_queue.queue) > 1:
        for campaign in campaign_queue.queue:
            searchads = SearchAd.objects.filter(campaign_id=campaign.id)
            for each_ad in searchads:
                ads_queue.queue.append(each_ad)
    else:
        for campaign in campaign_queue.queue:
            searchads = SearchAd.objects.filter(campaign_id=campaign[0].id)
            for each_ad in searchads:
                ads_queue.queue.append(each_ad)
    
    return ads_queue.queue
