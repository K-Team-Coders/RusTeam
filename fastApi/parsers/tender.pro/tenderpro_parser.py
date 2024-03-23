from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from loguru import logger
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
# Путь к исполняемому файлу ChromeDriver
driver_path = 'drivers\chromedriver.exe'

# Путь к исполняемому файлу браузера Chrome
chrome_binary_path = 'chrome-win64\chrome.exe'

# Создаем сервис для ChromeDriver
service = Service(driver_path)

# Создаем опции для браузера Chrome
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path  # Устанавливаем путь к исполняемому файлу браузера Chrome
# Включаем режим headless
# chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')
# Создаем драйвер Chrome с использованием сервиса и опций
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.tender.pro/api/tenders/list?sid=&company_id=&face_id=0&order=3&tender_id=&tender_name=&company_name=&good_name=&tender_type=90&tender_state=100&country=0&region=&basis=0&okved=&dateb=&datee=&dateb2=&datee2=')

buffer=[]
table=[]

#Функция для получения инфо о тедере 
def get_tender_info(url:str):
    one_lement={}

    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    #------------
    tender_name=soup.find(attrs={"class":{"text__word-break"}}).text
    one_lement["tender_name"]=tender_name
    #------------
    tags=soup.find_all(attrs={"class":{"tag__item__title"}})
    
    one_lement["data_created"]=tags[1].text
    one_lement["tender_id"]=tags[2].text
    one_lement["data_execution"]=tags[5].text

    documents=soup.find_all(attrs={"class":{"link _black2 text-d-ul"}})
    doc_buffer=[]
    for i in documents:
        doc_buffer.append("https://www.tender.pro"+i.get("href"))
    one_lement["documents"]=doc_buffer
    #------------
    organization=soup.find_all(attrs={"class":{"_black"}})
    one_lement["organization"]=organization[1].text
    #------------
    goods=soup.find_all(attrs={"class":{"_black text__word-break"}})
    # logger.debug(goods)
    goods_count=soup.select('.table-history-col.c-gray.text_center._fix-80.hide-sm')[2:]
    # logger.error(goods_count)
    goods_type=soup.select('.table-history-col.text_center._fix-80.hide-sm')[2:]
    # logger.debug(goods_type)
    goods_buffer=[]
    for i,j,k in zip(goods,goods_count,goods_type):
        goods_buffer.append([i.text,j.text,k.text])
    one_lement["goods"]=goods_buffer
    #------------
    logger.debug(one_lement)
    return one_lement

def get_urls(element:str,data_1:str,data_2:str):
    #ввод данных (название,дата начала и конец)
    input_element_good_name = driver.find_element(By.ID,"good_name_id")
    input_element_data_1=driver.find_element(By.ID,"date_1")
    input_element_data_2=driver.find_element(By.ID,"date_2")
    #отправляем в форму
    input_element_good_name.send_keys(element)
    input_element_data_1.send_keys(data_1)
    input_element_data_2.send_keys(data_2)
    show_button=driver.find_element(By.ID,"view_tenders_list-submit")

    show_button.submit()

    while True:
        try:
            products_url=driver.find_elements(By.CLASS_NAME,"tender__name-wrapper")
            for i in products_url:
                buffer.append(i.find_element(By.TAG_NAME,"a").get_attribute("href"))

                table.append(get_tender_info(i.find_element(By.TAG_NAME,"a").get_attribute("href")))



            #переход на следующую страницу
            next_element=driver.find_element(By.CLASS_NAME,"pagination__link.pagination__link_next").get_attribute("href")

            driver.get(next_element)
        except:
            break



if __name__=="__main__":
    result=get_urls("Арматура","10.02.2024","15.03.2024")
    df=pd.DataFrame(table)
    logger.info(df)
    df.to_csv("data.csv",sep=';',encoding = 'utf-8')
    time.sleep(11)
    driver.quit()