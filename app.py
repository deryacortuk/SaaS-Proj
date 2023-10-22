from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import re

text = "En cok sevdigim @eda.ece 'mle islim kebabi yaparken biraz dugun biraz ask biraz is konustuk, link bioda yayinda"
usernames = re.findall(r'@([a-zA-Z0-9._]+)', text)
print(usernames)
def login_inst():
    username = "oceanangel.ai" 
    password = "17ocean7@"
    url = "https://www.instagram.com/"
   
  
    
    options = Options()
     
    # options.add_argument('--headless=new')    
    # options.add_argument("start-maximized")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--proxy-server='direct://'")
    # options.add_argument("--proxy-bypass-list=*")
    # options.add_argument("--start-maximized")    
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/95.0.4638.69 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(5)
    user = driver.find_element(By.NAME, "username")
    user.send_keys(username)
    sleep(1)
    pwrd = driver.find_element(By.NAME,"password")
    pwrd.send_keys(password)
    sleep(1)    
    driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()
    sleep(7)
    driver.find_element(By.XPATH, '//section/main/div/div/div/div/div').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9_1').click()
    sleep(1)
    return driver
    
# print(login_inst())


# username = "silvakomsic"
username = "jeffbezos"

def get_instagram(username):
    
    driver = login_inst()
    # option = Options()
    # option.headless = False
    # driver = webdriver.Chrome(options=option)
    # driver.get(url)
    
    sleep(10)
    

    driver.find_element(By.CSS_SELECTOR,'.x1xgvd2v > div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > div:nth-child(1)').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,'input.x1lugfcp').send_keys(username)
    sleep(3)

    driver.find_element(By.CSS_SELECTOR,'a.x1dm5mii:nth-child(1) > div:nth-child(1)').click()
    sleep(10)
    
    
    profile = {}
    
    ul_element = driver.find_element(By.CSS_SELECTOR,'ul.x78zum5')
    
    li_elements = ul_element.find_elements(By.TAG_NAME,'li')
    
    for li_element in li_elements:        
        span_element = li_element.find_element(By.TAG_NAME,'span')
        text = span_element.text
        
        li_text = li_element.text
        data = li_text.split()
        profile[data[1]] = text
    
    div_element = driver.find_element(By.CSS_SELECTOR,'.x7a106z')
    span_info = div_element.find_element(By.CSS_SELECTOR,'span')
    h1_element = div_element.find_element(By.CSS_SELECTOR,'h1')
    
    profile["full_name"] = span_info.text
    profile["public_figure"] = h1_element.text
    
    posts = list()
    
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    # repeat_count = 3

    # for _ in range(repeat_count): 
       
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    #     sleep(1)
    
    private_account = ""
    try:
        element = driver.find_element(By.CSS_SELECTOR,'div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > div._aady._aa_s > div > h2')
        if element:
            private_account = element.text
        else:
            user_infos = driver.find_element(By.CSS_SELECTOR,"article.x1iyjqo2") 
            sleep(5)
            user_posts = user_infos.find_elements(By.CSS_SELECTOR,'div._ac7v._al3n') 
    except NoSuchElementException:
        print("Element was not found!")
        
    profile["is_private"] = private_account or "Public account"
    # driver.execute_script("window.scrollBy(0,1000000)")

    # sleep(5)
    # user_infos = driver.find_element(By.CSS_SELECTOR,"article.x1iyjqo2") 
    # sleep(5)
    # user_posts = user_infos.find_elements(By.CSS_SELECTOR,'div._ac7v._al3n')             
    
    # sleep(5)
    
    # print(len(user_posts))
    
    # for post in user_posts: 
    #     sleep(1)       
    #     elements = post.find_elements(By.CSS_SELECTOR, "div._aabd._aa8k._al3l")
    #     sleep(1)
    #     actions = ActionChains(driver)
    #     sleep(1)
        
    #     for info in elements:
    #         temp = {}
            
    #         actions.move_to_element(info).perform()
            
    #         href = info.find_element(By.TAG_NAME,"a").get_attribute("href")
    #         img = info.find_element(By.TAG_NAME, "img").get_attribute("alt")
            
            
    #         hidden_element = info.find_element(By.CLASS_NAME, "_ac2d")  
            
    #         li_elements = hidden_element.find_elements(By.CLASS_NAME, "_abpm")  
            
            
    #         temp["href"] = href
    #         temp["tag"] = img
    #         if len(li_elements) >= 2:
    
    #             temp["likes"] = li_elements[0].find_element(By.TAG_NAME, "span").text
    
    
    #             temp["comments"] = li_elements[1].find_element(By.TAG_NAME, "span").text
  
                
    #         posts.append(temp) 
    #         print(temp)     
        
                                                                     
                                  
    # print(posts)     
    print(profile)
    driver.quit()







    # description_element = driver.find_element(By.CSS_SELECTOR,'ul.x78zum5')

    
    # description_content = description_element.get_attribute("content")
    # followers = re.search(r'(\w+) Followers', description_content).group(1)
    # following = re.search(r'(\w+) Following', description_content).group(1)
    # posts = re.search(r'(\w+) Posts', description_content).group(1)
    
    # pattern = r'See Instagram photos and videos from (.*?) \(@([\w]+)\)'
    # match = re.search(pattern, description_content)
    
    
    # if match:
        
    #     name = match.group(1)  
    #     username = match.group(2)  
    #     profile["full_name"] = name
    #     profile["username"] = username
    #     profile["followers"] = followers
    #     profile["following"] = following
    #     profile["posts"] = posts
    # else:
    #     print("There is match!")
        
    # ul_element = driver.find_element(By.CLASS_NAME, '_abpo')


    # li_elements = ul_element.find_elements(By.CLASS_NAME,'_abpm')

    # for li_element in li_elements:
    #     span_elements = li_element.find_elements(By.CSS_SELECTOR,'span')
    #     for span_element in span_elements:
    #         print(span_element.text)
