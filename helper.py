from collections import Counter
import re
import json
import time
import ast
from datetime import datetime, timedelta
start_time = time.time()




def find_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return list(set(hashtags)) or []
    

def find_usernames(text):
    usernames = re.findall(r'@([a-zA-Z0-9._]+)', text)
    
    return list(set(usernames)) or []

def hashtag_count(username):
    with open(f"userHubData/{username}-detail-posts.json", "r", encoding="utf-8") as file:
        userdata = file.read()
        user_data = ast.literal_eval(userdata)
    
    all_hashtags = []
    for post in user_data:
        hashtags = post.get('hashtags', [])
        all_hashtags.extend(hashtags)
    hashtags_count = Counter(all_hashtags)
    top_10_hashtags = hashtags_count.most_common(10)
    hashtag_list = {}
    for hashtag, count in top_10_hashtags:
        hashtag_list[hashtag] = count
    return hashtag_list

def user_tags_count(username):
    with open(f"userHubData/{username}-detail-posts.json", "r", encoding="utf-8") as file:
        userdata = file.read()
        user_data = ast.literal_eval(userdata)
    
    all_tags = []
    for post in user_data:
        all_tags.extend(post["tags"])

    tag_counts = Counter(all_tags)
    top_tags = tag_counts.most_common(10)
    
    user_tag = {}
    for tag, count in top_tags:
        user_tag[tag] = count
    return user_tag

def str_to_int(data):
    number = data.replace(',', '').replace('.', '')
    if number[-1] == 'M':
        return int(float(number[:-1]) * 1000000)  
    elif number[-1] == 'K':
        return int(float(number[:-1]) * 1000) 
    else:
        return int(number)



def calculate_engagement_rate(username):
    with open(f"userHubData/{username}-posts.json", "r", encoding="utf-8") as file:
        user_profile = json.load(file)
    user_followers = user_profile["profile"]["followers"]
    
    followers = str_to_int(user_followers)
    
    with open(f"userHubData/{username}-detail-posts.json", "r", encoding="utf-8") as file:
        userdata = file.read()
        user_data = ast.literal_eval(userdata)
        
    result = 0
    
    for data in user_data:
         
        result += data["engagement_rate"]
   
    engagement_rate = round(((result/len(user_data))/followers) * 100,3)
    return engagement_rate
        
    
def reels_engagement_rate(username):
    with open(f"userHubData/{username}-posts.json", "r", encoding="utf-8") as file:
        user_profile = json.load(file)
    user_followers = user_profile["profile"]["followers"]
    
    followers = str_to_int(user_followers)
    
    with open(f"userHubData/{username}-reels-data.json","r", encoding="utf-8") as file:
        reelsdata = file.read()         
        user_data = ast.literal_eval(reelsdata)
    result = 0
    for data in user_data:
        result += data["engagement_rate"]
    
    engagement_rate = round(((result/len(user_data))/followers) * 100,3)
    return engagement_rate
        
def max_engagement_rate_posts(username):
    with open(f"userHubData/{username}-detail-posts.json", "r", encoding="utf-8") as file:
        userdata = file.read()
        user_data = ast.literal_eval(userdata)
        
    sorted_data = sorted(user_data, key=lambda x: x.get("engagement_rate", 0), reverse=True)[:10]
    
    return sorted_data
    


def max_reels_engagement_rate(username):
    with open(f"userHubData/{username}-reels-data.json","r", encoding="utf-8") as file:
        reelsdata = file.read()         
        user_data = ast.literal_eval(reelsdata)
    sorted_data = sorted(user_data, key=lambda x: x.get("engagement_rate", 0), reverse=True)[:10]
    
    return sorted_data



def parse_date(date_string):
    current_date = datetime.now()

    if "minutes ago" in date_string:
        minutes_ago = int(re.search(r'\d+', date_string).group())
        return current_date - timedelta(minutes=minutes_ago)
    elif "hours ago" in date_string:
        hours_ago = int(re.search(r'\d+', date_string).group())
        return current_date - timedelta(hours=hours_ago)
    elif "days ago" in date_string:
        days_ago = int(re.search(r'\d+', date_string).group())
        return current_date - timedelta(days=days_ago)
    elif "," in date_string:
        try:
           
            formatted_date = datetime.strptime(date_string, "%B %d, %Y")
            return formatted_date
        except ValueError:
            return None
    else:
        try:
            
            formatted_date = datetime.strptime(date_string, "%B %d")
            if formatted_date.month > current_date.month or (formatted_date.month == current_date.month and formatted_date.day > current_date.day):
               
                return formatted_date.replace(year=current_date.year - 1)
            else:
                return formatted_date.replace(year=current_date.year)
        except ValueError:
            return None
        
def sorted_date(username):
    with open(f"userHubData/{username}-detail-posts.json", "r", encoding="utf-8")  as file:
        userdata = file.read()
        user_data = ast.literal_eval(userdata)       

    sorted_user_data = sorted([(parse_date(date_string["time"]), date_string) for date_string in user_data], key=lambda x: x[0],reverse=True)
    sorted_user_data = [item[1] for item in sorted_user_data if item[0] is not None]
    
    return sorted_user_data[:2]
    
# print(hashtag_count("jeffbezos"))
# print(user_tags_count("jeffbezos"))
# print(calculate_engagement_rate("jeffbezos"))
# print(reels_engagement_rate("jeffbezos"))
# print(max_engagement_rate_posts("jeffbezos"))
# print(max_reels_engagement_rate("jeffbezos"))
print(sorted_date("jeffbezos"))


