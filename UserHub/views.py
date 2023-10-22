from django.shortcuts import render
from .scraping import get_instagram
from .helper import max_engagement_rate_posts, max_reels_engagement_rate, hashtag_count,user_tags_count, calculate_engagement_rate, reels_engagement_rate,sorted_date,str_to_int
from django.http import JsonResponse
from .tasks import celery_tasks_posts,get_instagram_task

import json

def instagram_discovery(request):
    if request.method == "POST":
        username = request.POST.get('username')
        
        get_instagram_task.delay(username)
        
        
        #celery_tasks_posts.delay(username)
        
        
        return JsonResponse({"result":"success"})
    else:
        return render(request,"userhub/discovery.html")




def analyze_user(request, username):
    with open(f"userHubData/{username}-posts.json","r",encoding="utf-8") as file:
        user = json.load(file)
    profile = user["profile"]
    followers = str_to_int(user["profile"]["followers"])
    user_data = sorted_date(username)
    for data in user_data:
        data["post_rate"] = round((data["engagement_rate"]/followers) * 100,2)
        
    max_posts= max_engagement_rate_posts(username)
    for data in max_posts:
        data["post_rate"] = round((data["engagement_rate"]/followers) * 100,2)
    max_reels = max_reels_engagement_rate(username)
    for data in max_reels:
        data["reel_rate"] = round((data["engagement_rate"]/followers) * 100,2)
    hashtags = hashtag_count(username)
    captions = user_tags_count(username)
    total_engagement_rate = calculate_engagement_rate(username)
    reels_total_rate = reels_engagement_rate(username)
    
    
    return render(request, "userhub/analyse.html",{"profile":profile,"data":user_data,"max_posts":max_posts,"max_reels":max_reels,"hashtags":hashtags,"captions":captions,"engagement_rate":total_engagement_rate,"reels_rate":reels_total_rate})
    
    
