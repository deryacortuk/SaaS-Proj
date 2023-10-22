from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import ast
import json


import re

# Veri örneği
veri = "507,833 views"

# Views değerini ayıklayan regex ifadesi
views_pattern = r'([\d,]+) views'

# Likes değerini ayıklayan regex ifadesi (eğer varsa)
likes_pattern = r'([\d,]+) likes'

# Views değerini ayıkla
views_match = re.search(views_pattern, veri)
if views_match:
    views = views_match.group(1).replace(',', '')  # Virgülleri temizle ve views değerini al

# Likes değerini ayıkla (eğer varsa)
likes_match = re.search(likes_pattern, veri)
if likes_match:
    likes = likes_match.group(1).replace(',', '')  # Virgülleri temizle ve likes değerini al

# Sonuçları görüntüle
print("Views:", views)
if 'likes' in locals():
    print("Likes:", likes)

# url_list_new = ["https://www.instagram.com/p/CgU1xsqldj7/","https://www.instagram.com/p/Cf_g7RWlObD/","https://www.instagram.com/p/CfFI0MXljjN/", 'https://www.instagram.com/p/Cf_g7RWlObD/', 'https://www.instagram.com/p/CfRr5kYp-WN/', 'https://www.instagram.com/p/CfF2KMJuaMG/', 'https://www.instagram.com/p/CfFI0MXljjN/', 'https://www.instagram.com/p/CfASkCKPCpA/', 'https://www.instagram.com/p/CeaGmYEl61v/', 'https://www.instagram.com/p/Cdn0mzvLDBp/', 'https://www.instagram.com/p/CdgR1nGFjit/']
def get_posts():       
    with open("jeffbezos-posts-urls.txt", "r") as file:
        urls_str = file.read()
        urls_list = ast.literal_eval(urls_str)
        
    posts = [] 
#     mobile_emulation = {
#     "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
#     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
# }   
    options = Options()
        
    # options.add_argument('--headless')    
    # options.add_argument("--disable-extensions")
    # options.add_argument("--proxy-server='direct://'")
    # options.add_argument("--proxy-bypass-list=*")
    # options.add_argument("--start-maximized")    
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--log-level=1')
    mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}   
    options.add_experimental_option("mobileEmulation", mobile_emulation)  
    driver = webdriver.Chrome(options=options)
    for url in urls_list:               
        try:  
            post = {}                 
            driver.get(url)
            print(url)
            sleep(10)
            
            
            
            user_post = driver.find_element(By.CSS_SELECTOR,'div:nth-child(1) > div > article._aa6a._aatb._aatd._aatf')
            #user_post = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "article._aa6a._aatb._aatd._aatf")))
            post_title = user_post.find_element(By.CSS_SELECTOR, 'div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x12nagc.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > span:nth-child(4) > h1') 
            #post_username = WebDriverWait(user_post, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._a9zr > div._a9zs > h1')))
            post_time = user_post.find_element(By.CSS_SELECTOR, 'div._akdp > div > div > a > span > time')
            #post_time = WebDriverWait(user_post, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._ae2s._ae3v._ae3w > div._ae5u._ae5v._ae5w > div > div > a > span')))
            
            post_views = user_post.find_element(By.CSS_SELECTOR, 'section._ae5m')
            #post_likes = WebDriverWait(user_post, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.x1a02dak.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1 > span > a > span > span')))
            post_comments = user_post.find_element(By.CSS_SELECTOR,'div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x12nagc.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1 > a > span > span')
            post["url"] = url
            post["time"] = post_time.text
            post["title"] = post_title.text
            post["views"] = post_views.text
            post["comments"] = post_comments.text            
            posts.append(post)            
            print(post)
            sleep(1)
        except Exception as e:
            print(f"Error: {e}")
    
    with open("user-posts.json","w",encoding="utf-8") as file:
        file.write(str(posts))
        
    driver.quit()
    
    
    #user_post = driver.find_element(By.CSS_SELECTOR,'')
    

get_posts()


def get_login():
    pass
url = "https://www.instagram.com/jeffbezos/reels"

def get_reels(username):
    options = Options()   
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    sleep(5)       

    # driver.find_element(By.CSS_SELECTOR,'div.x6s0dn4.xcfux6l.x1qhh985.xm0m39n.x9f619.x1w9h7q7.x78zum5.x1q0g3np.x2lah0s.x1pg5gke.xwhw2v2.xl56j7k.x1r0g7yl.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x2b8uid.x11njtxf.x5ur3kl.x13fuv20.x178xt8z > a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._aa-z._aa--._ac_u._a6hd > div').click()
    
    # sleep(10)
    
    
    
    
    reels_urls = list()    
    sleep(5)
    
    # user_reels = driver.find_element(By.CSS_SELECTOR,'div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1')
    last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    user_reels = driver.find_elements(By.TAG_NAME,"a")
    while True:
        driver.execute_script("return document.body.scrollHeight")
        sleep(5)       
                                 
        #href = info.find_elements(By.TAG_NAME,"a")                                                        
                    
        for link in user_reels:           
            temp = {}
            if  link.get_attribute("href"):
                if "https://www.instagram.com/reel/" in link.get_attribute("href"):
                    
                    temp["href"] = link.get_attribute("href")
                    
                    user_element = link.find_element(By.CSS_SELECTOR, 'div._aaj-')  
                    ul_element = user_element.find_element(By.CSS_SELECTOR, 'ul._abpo')

                               
                    li_elements = ul_element.find_elements(By.TAG_NAME, "li")                      
                    
                    likes_span_element = li_elements[0].find_elements(By.TAG_NAME, 'span')[0]
                    likes = likes_span_element.text
                    temp["likes"] =likes
                    comments_span_element = li_elements[1].find_elements(By.TAG_NAME, 'span')[0]
                    comments = comments_span_element.text
                    temp["comments"] =comments                                                             
                                                                                
                    watch_reel = link.find_element(By.CSS_SELECTOR, 'div._aaj_')
                    temp["watch"] = watch_reel.find_element(By.TAG_NAME,"span").text
                                    
                    print(temp)    
                    reels_urls.append(temp)
                
        last_count = last_height
        sleep(2)
        last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        if last_count==last_height:
            break                 
    
    with open(f"{username}-reels.txt","w", encoding="utf-8") as file:
        file.write(str(reels_urls))     

# get_reels("jeff")
# driver = webdriver.Chrome()
# driver.get("https://www.example.com")
# posts = []

# while True:
#     # Scrolldown yaparak sayfanın en altına inin
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(2)  # Sayfa tam yüklenmesi için bir süre bekle

#     # user_infos elementini bulun
#     user_infos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "article.x1iyjqo2")))

#     # user_posts listesini alın
#     user_posts = WebDriverWait(user_infos, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._ac7v._al3n")))

#     for post in user_posts:
#         # Post elementine hover yapın
#         ActionChains(driver).move_to_element(post).perform()

#         # Gerekli verileri alın
#         temp = {}
#         hidden_element = WebDriverWait(post, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_ac2d")))
#         li_elements = hidden_element.find_elements(By.CLASS_NAME, "_abpm")

#         if len(li_elements) >= 2:
#             temp["likes"] = li_elements[0].find_element(By.TAG_NAME, "span").text
#             temp["comments"] = li_elements[1].find_element(By.TAG_NAME, "span").text

#         posts.append(temp)

#     # Sayfa sonuna ulaşıldıysa döngüyü sonlandır
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break

# # Alınan verileri işleyebilir veya yazdırabilirsiniz
# for post in posts:
#     print(post)

# # Tarayıcı penceresini kapat
# driver.quit()
