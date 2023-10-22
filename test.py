# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from time import sleep
# import random
# import ast
# from concurrent.futures import ThreadPoolExecutor
# import json
# import re
# from helper import find_hashtags, find_usernames
# from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
# import concurrent.futures
    
# import time

# start_time = time.time()
# username = "jeffbezos"
# user = [
#     ("sellorbuy.shop","17derya17@")  #, ("oceanangel.ai","17ocean7@")
# ]

# random_user = random.choice(user)

# def login_instagram():
#     print(random_user)
#     url = "https://www.instagram.com/"      
#     options = Options()     
#     options.add_argument('--headless=new')    
#     options.add_argument("start-maximized")
#     options.add_argument("--window-size=1920,1080")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--proxy-server='direct://'")
#     options.add_argument("--proxy-bypass-list=*")
#     options.add_argument("--start-maximized")    
#     options.add_argument('--disable-gpu')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--allow-running-insecure-content')   
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/95.0.4638.69 Safari/537.36")
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     sleep(3)
#     user = driver.find_element(By.NAME, "username")
    
#     user.send_keys(random_user[0])
#     sleep(1)
#     pwrd = driver.find_element(By.NAME,"password")
    
#     pwrd.send_keys(random_user[1])
#     sleep(1)    
#     driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
#     sleep(5)
#     driver.find_element(By.XPATH, '//section/main/div/div/div/div/div').click()
#     sleep(3)
#     driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9_1').click()
#     sleep(1)
#     print("success")
#     return driver


# def get_reels(username,driver):
    
    
#     url = f"https://www.instagram.com/{username}/reels" 
#     driver.get(url)    
#     sleep(2)                        
             
#     reels_urls = []
#     last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#     user_infos = driver.find_element(By.CSS_SELECTOR,'div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1')
#     reels_links = set()
    
#     while True:
#         driver.execute_script("return document.body.scrollHeight")
#         sleep(2)                                        
                                                            
#         user_reels = user_infos.find_elements(By.TAG_NAME,"a")
#         sleep(2)     
        
#         for link in user_reels:           
            
#             if  link.get_attribute("href"):
#                 if "https://www.instagram.com/reel/" in link.get_attribute("href"):
                    
#                     if link.get_attribute("href") not in reels_links:
#                         temp = {}
#                         reels_links.add(link.get_attribute("href"))
#                         temp["url"] = link.get_attribute("href")                     
                                                                                                                                                                          
#                         li_elements = driver.execute_script("""
#         var anchorElement = arguments[0];
#         var liElements = anchorElement.querySelectorAll("li");
#         var items = [];       
        
#         var likeText = liElements[0].querySelector("span").textContent;
#         var commentText = liElements[1].querySelector("span").textContent;
        
#         items.push({"likes": likeText, "comments": commentText});
        
#         return items;""", link)

                                            
#                         temp["likes"] = li_elements[0]["likes"] 
#                         temp["comments"] = li_elements[0]["comments"]                                         
#                         watch_reel = link.find_element(By.CSS_SELECTOR, 'div._aaj_')
#                         temp["watch"] = watch_reel.find_element(By.TAG_NAME,"span").text                        
#                         reels_urls.append(temp)                                                       
#         last_count = last_height
#         sleep(2)
        
#         last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#         if len(reels_urls) >= 100:
#             break
#         if last_count==last_height:
#             break                 
   
#     with open(f"{username}-reels-data.json","w", encoding="utf-8") as file:
#         json_data = json.dumps(reels_urls, indent=4)                
#         file.write(json_data)
#     #driver.quit()  
#     return "Success"

# def get_instagram(username, driver):
    
#     #driver = login_instagram()  
    
#     sleep(1)
    

#     driver.find_element(By.CSS_SELECTOR,'.x1xgvd2v > div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > div:nth-child(1)').click()
#     sleep(2)
#     driver.find_element(By.CSS_SELECTOR,'input.x1lugfcp').send_keys(username)
#     sleep(3)

#     driver.find_element(By.CSS_SELECTOR,'a.x1dm5mii:nth-child(1) > div:nth-child(1)').click()
#     sleep(3)
    
    
#     profile = {}
#     div_element = driver.find_element(By.CSS_SELECTOR,'.x7a106z')
#     span_info = div_element.find_element(By.CSS_SELECTOR,'span')
#     h1_element = div_element.find_element(By.CSS_SELECTOR,'h1')
    
    
#     profile["username"] = username
#     profile["full_name"] = span_info.text
#     profile["public_figure"] = h1_element.text                      
    
    
#     ul_element = driver.find_element(By.CSS_SELECTOR,'ul.x78zum5')
    
#     li_elements = ul_element.find_elements(By.TAG_NAME,'li')
    
#     for li_element in li_elements:        
#         span_element = li_element.find_element(By.TAG_NAME,'span')
#         text = span_element.text
        
#         li_text = li_element.text
#         data = li_text.split()
#         profile[data[1]] = text   
        
#     post_urls = []     
#     user_data = {}
#     infos = []
#     private_account = ""
#     try:
#         element = driver.find_element(By.CSS_SELECTOR,'div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > div._aady._aa_s > div > h2')
#         if element:
#             private_account = element.text
#             img_el = driver.find_element(By.CSS_SELECTOR,'section > main > div > header > div > div > div > button > img')
#             profile["profile_img"] = img_el.get_attribute("src")
        
            
#     except NoSuchElementException:
#         print("Element was not found!")
#         img_el = driver.find_element(By.CSS_SELECTOR,'header > div > div > span > img')
#         profile["profile_img"] = img_el.get_attribute("src")
#         last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#         user_infos = driver.find_element(By.CSS_SELECTOR,"article.x1iyjqo2")    
                    
#         while True:
#             driver.execute_script("return document.body.scrollHeight")
#             sleep(1)                       
#             user_posts = user_infos.find_elements(By.CSS_SELECTOR,'div._ac7v._al3n')
#             sleep(1)
        
        
#             for info in user_posts:            
            
#                 href = info.find_elements(By.TAG_NAME,"a")                                                        
#                 sleep(1)  
#                 for hr in href:           
                
#                     if hr.get_attribute("href") not in post_urls:
#                         post = dict()
#                         post_urls.append(hr.get_attribute("href")) 
#                         img_element = hr.find_element(By.TAG_NAME,"img")
#                         img_src = img_element.get_attribute("src")
#                         post["url"] = hr.get_attribute("href") 
#                         post["img_src"] = img_src                                                                             
#                         infos.append(post)
                        
#             last_count = last_height
#             sleep(2)
#             last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#             if len(post_urls) >= 100:
#                 break
#             if last_count==last_height:
#                 break   
        
#     profile["is_private"] = private_account or "Public account" 
#     user_data["profile"] = profile              
#     print(profile)
#     if profile["is_private"] == "Public account":
#         user_data["posts"] = infos
        
#         with open(f"{username}-posts-urls.txt","w", encoding="utf-8") as file:
#             file.write(str(post_urls)) 
#         # get_reels(username, driver)
    
#     with open(f"{username}.posts.json", "w", encoding="utf-8") as file:
#         json_data = json.dumps(user_data,indent=4)                
#         file.write(json_data)
#     #driver.quit()
#     return "Success"
    
# def get_process(username):
#     driver = login_instagram()
    
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.submit(get_instagram, username,driver)
#         executor.submit(get_reels, username,driver)
        
        
#     driver.quit()

    
        
# if __name__ == "__main__":
#     get_process(username)
#     finish_time = time.time()
#     print((finish_time - start_time) / 60)
