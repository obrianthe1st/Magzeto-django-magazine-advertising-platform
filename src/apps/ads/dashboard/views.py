from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from apps.ads.analytics.utils import campaign_analytics, display_ads

# Create your views here.

@login_required
def dashboard_view(request):
    campaign_s =  campaign_analytics.get_campaigns_data(request)
    campaign_data = campaign_analytics.get_ad_data(campaign_s)
    data = []

    campaigns = list((campaign_analytics.top_3_performing_campaigns(request).items()))
    for i in campaigns:
        data.append(i)
    
    context={'data':data}
    return render(request,'ads/dashboard.html',context)

def helloWorld(request):
    return JsonResponse({'text':'hello world'})

def showAnalyticsData(request):
    campaign_s =  campaign_analytics.get_campaigns_data(request)
    campaign_data = campaign_analytics.get_ad_data(campaign_s)

    analytics_data = {}


    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        dateType = int(request.POST.get('dateType'))
        print(dateType)

        if dateType == 7:
            analytics_data = {"spend_data" : campaign_analytics.get_spend_data(request,days=dateType,campaign_data=campaign_data),
            "clicks_data": campaign_analytics.get_clicks_data(request,days=dateType,campaign_data=campaign_data),
            "impressions_data" : campaign_analytics.get_impressions_data(request,days=dateType,campaign_data=campaign_data),
            "imp_vs_clicks" : campaign_analytics.impressions_VS_clicks_data(request,days=dateType,campaign_data=campaign_data)}
            return JsonResponse({'type':dateType,'data':analytics_data})
        elif dateType == 1:
            analytics_data = {"spend_data" : campaign_analytics.get_spend_data(request,days=30,campaign_data=campaign_data),
            "clicks_data": campaign_analytics.get_clicks_data(request,days=30,campaign_data=campaign_data),
            "impressions_data" : campaign_analytics.get_impressions_data(request,days=30,campaign_data=campaign_data),
            "imp_vs_clicks" : campaign_analytics.impressions_VS_clicks_data(request,days=30,campaign_data=campaign_data)}
            return JsonResponse({'type':dateType,'data':analytics_data})
        else:
            analytics_data = {"spend_data" : campaign_analytics.get_spend_data(request,month=dateType,campaign_data=campaign_data),
            "clicks_data": campaign_analytics.get_clicks_data(request,month=dateType,campaign_data=campaign_data),
            "impressions_data" : campaign_analytics.get_impressions_data(request,month=dateType,campaign_data=campaign_data),
            "imp_vs_clicks" : campaign_analytics.impressions_VS_clicks_data(request,month=dateType,campaign_data=campaign_data)}
            return JsonResponse({'type':dateType,'data':analytics_data})

    return redirect('dashboard')
