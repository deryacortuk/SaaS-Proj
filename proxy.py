# from seleniumwire import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# import random
import redis


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

queue_name = 'celery'

redis_client.delete(queue_name)

print(f'Kuyruk "{queue_name}" temizlendi.')

# # the list of proxy to rotate on 
# PROXIES = [
#     'http://19.151.94.248:88',
#     # 'http://149.169.197.151:80',
#     # ...
#     'http://212.76.118.242:97'
# ]

# # randomly extract a proxy
# random_proxy = random.choice(PROXIES)

# # set the proxy in Selenium Wire
# seleniumwire_options = {
#     'proxy': {
#         'http': f'{random_proxy}',
#         'https': f'{random_proxy}',
#         'verify_ssl': False,
#     },
# }

# # create a ChromeDriver instance
# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()),
#     seleniumwire_options=seleniumwire_options
# )

# driver.visit('https://example.com/')

# # scraping logic...

# driver.quit()

# # visit other pages...



#     while True:                      
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(5)
             
        
#         user_posts = user_infos.find_elements(By.CSS_SELECTOR,'div._ac7v._al3n')               
#         sleep(1)
                   
        
#         for post in user_posts:             
#             sleep(1)   
#             elements = post.find_elements(By.CSS_SELECTOR, "div._aabd._aa8k._al3l")
#             sleep(1)
            
           
                
#             for info in elements:                
#                 temp = {}
                
            
#                 href = info.find_element(By.TAG_NAME,"a").get_attribute("href")
#                 img = info.find_element(By.TAG_NAME, "img").get_attribute("alt")
#                 temp["href"] = href
#                 temp["tag"] = img
#                 actions = ActionChains(driver)                
#                 actions.move_to_element(info)
#                 hidden_element = info.find_element(By.CLASS_NAME, "_ac2d")  
            
#                 li_elements = hidden_element.find_elements(By.CLASS_NAME, "_abpm")  
            
            
                
#                 if len(li_elements) >= 2:
    
#                     temp["likes"] = li_elements[0].find_element(By.TAG_NAME, "span").text
    
    
#                     temp["comments"] = li_elements[1].find_element(By.TAG_NAME, "span").text
  
#                 actions.release(info)
                
#                 posts.append(temp) 
#                 print(temp)   
            
#         new_height = last_height
#         sleep(5)      
#         last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#         sleep(1)
#         if new_height == last_height:            
#             break
        
        
        
#         while True:
        
#         ActionChains(driver).move_to_element(user_infos).perform()
#         # user_posts = user_infos.find_elements(By.CSS_SELECTOR,'div._ac7v._al3n')            
        
#         user_posts = WebDriverWait(user_infos, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._ac7v._al3n")))
        
#         for infos in user_posts:   
#             ActionChains(driver).move_to_element(infos).perform()
#             # elements = infos.find_elements(By.CSS_SELECTOR, "div._aabd._aa8k._al3l")
            
#             elements = WebDriverWait(infos, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._aabd._aa8k._al3l")))
            
#             for info in elements:                
#                 temp = {}                                                                 
#                 ActionChains(driver).move_to_element(info).perform()
                
#                 hidden_element = WebDriverWait(info, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "_ac2d")))  #info.find_element(By.CLASS_NAME, "_ac2d")  
            
#                 li_elements = hidden_element.find_elements(By.CLASS_NAME, "_abpm")  
            
            
                
#                 if len(li_elements) >= 2:
                    
    
#                     temp["likes"] = li_elements[0].find_element(By.TAG_NAME, "span").text
    
    
#                     temp["comments"] = li_elements[1].find_element(By.TAG_NAME, "span").text
#                 print(temp["likes"])
                
                
#                 posts.append(temp) 
                
#             last_count = last_height
#             sleep(10)           
                  
        
#         last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#         if last_count==last_height:
#             break    