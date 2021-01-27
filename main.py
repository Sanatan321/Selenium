import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tqdm import tqdm


driver = webdriver.Chrome('F://sanatan//Python workSpace//chromedriver')
driver.set_window_size(1920, 1080)
driver.get("https://www.flipkart.com/")


mobile='123456'
password='9876654'

body = driver.find_element_by_tag_name('body')
main_block = body.find_element_by_class_name('mCRfo9')
loginform = main_block.find_element_by_tag_name('form')
input= loginform.find_elements_by_tag_name('input')


mobl=input[0]
mobl.clear()
mobl.send_keys(mobile)
mobl.send_keys(Keys.RETURN)
pswrd = input[1]
pswrd.clear()
pswrd.send_keys(password)
pswrd.send_keys(Keys.RETURN)
loginform.find_element_by_tag_name('button').click()
driver.get("https://www.flipkart.com/")

driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/ul/li[1]/span//*[name()="svg"]').click()
container=driver.find_element_by_id('container')
category=container.find_element_by_class_name('_114Zhd')
electrncs=category.find_element_by_tag_name('li')

x=electrncs.find_element_by_class_name('QPOmNK')
li=x.find_elements_by_tag_name('li')
infinix=li[4]
from selenium.webdriver.common.action_chains import ActionChains

#element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]/div/ul/li[1]/ul/li/ul/li[1]/ul/li[4]/a'))
#WebDriverWait(driver, 10).until(element_present)
button=infinix.find_element_by_tag_name('a')
#driver.implicitly_wait(10)
#ActionChains(driver).move_to_element(button).click(button).perform()

url=button.get_attribute('href')
driver.get(url)
linklist=[]

while True :
   # driver.get(url)
    prdct = driver.find_elements_by_class_name('_3O0U0u')
    for elmnt in prdct:
        tag=elmnt.find_element_by_tag_name('a')
        linklist.append(tag.get_attribute('href'))
    z=driver.find_elements_by_class_name('_3fVaIS')[-1]
    txt=z.find_element_by_tag_name('span').text
    if txt == 'NEXT':
        nxturl=z.get_attribute('href')
        driver.get(nxturl)
        #z.click()
    else:
        break

data=[]
for i in tqdm(linklist):
    driver.get(i)
    driver.implicitly_wait(10)
    name=driver.find_element_by_class_name('_35KyD6').text
    price=driver.find_element_by_class_name('_1uv9Cb').find_element_by_tag_name('div').text[1:]
    rating=driver.find_element_by_class_name('_2_KrJI').find_element_by_tag_name('div').text
    nrating=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[1]').text
    nreview=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[3]').text
    temp={'Name':name,
          'Price': price,
          'Rating': rating,
          'Number Of Rating': nrating,
          'Number Of Reviews': nreview,
          'Link': i}
    data.append(temp)

df=pd.DataFrame(data)
df.to_csv('F://sanatan//Python workSpace//data.csv')
#print(len(linklist))
#print(txt)

#print(url)


