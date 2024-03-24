from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from loguru import logger
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
from pathlib import Path


class TenderScraper:
    def __init__(self, driver_path,chrome_binary_path):
        # Создаем сервис для ChromeDriver
        self.service = Service(driver_path)
        
        # Создаем опции для браузера Chrome
        self.chrome_options = Options() # Устанавливаем путь к исполняемому файлу браузера Chrome
        self.chrome_options.add_argument('log-level=3')
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.binary_location = chrome_binary_path 
        self.table=[]
        self.buffer=[]
        self.current_datetime = datetime.now()
        self.formatted_date = self.current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

        # Создаем драйвер Chrome с использованием сервиса и опций
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        
        # self.driver.get('https://www.tender.pro/api/tenders/list?sid=&company_id=&face_id=0&order=3&tender_id=&tender_name=&company_name=&good_name=&tender_type=90&tender_state=100&country=0&region=&basis=0&okved=&dateb=&datee=&dateb2=&datee2=')

    def get_tender_info(self, url):
        one_element = {}

        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        try:
            error_elem = soup.find_all(string="Этот конкурс является закрытым")
            logger.success(f"Закрыт ли конкурс: {error_elem}")
        except: 
            pass
        
        logger.error(error_elem)
        if len(error_elem) != 0:
            one_element["tender_name"] = "Конкурс закрыт без приглашения"
            one_element["tender_id"] = "Конкурс закрыт без приглашения"
            one_element["organization"] = "Конкурс закрыт без приглашения"
            one_element["goods"] = "Конкурс закрыт без приглашения"
            one_element["documents"] = "Конкурс закрыт без приглашения"
            one_element["data_execution"] = "Конкурс закрыт без приглашения"
            one_element["data_created"] = "Конкурс закрыт без приглашения"
            logger.error(f"Конкурс закрыт: {one_element}")
            return one_element
        else:
                #------------
                tender_name=soup.find(attrs={"class":{"text__word-break"}}).text
                one_element["tender_name"]=tender_name
                #------------
                tags=soup.find_all(attrs={"class":{"tag__item__title"}})
                
                one_element["data_created"]=tags[1].text
                one_element["tender_id"]=tags[2].text
                one_element["data_execution"]=tags[5].text

                documents=soup.find_all(attrs={"class":{"link _black2 text-d-ul"}})
                doc_buffer=[]
                for i in documents:
                    doc_buffer.append({"name": i.text, "url": "https://www.tender.pro"+i.get("href")})
                one_element["documents"]=doc_buffer
                #------------
                organization=soup.find_all(attrs={"class":{"_black"}})
                one_element["organization"]=organization[1].text

                goods=soup.find_all("div",class_="table-history")[0].find_all(attrs={"class":{"_black text__word-break"}})

                goods_count=soup.find_all("div", class_="table-history-col c-gray text_center _fix-80 hide-sm")[2:]
                
                # logger.warning(goods_count)
                goods_type=soup.find_all("div",class_="table-history-col text_center _fix-80 hide-sm")
                
                goods_buffer=[]
                for good, good_count, good_type in zip(goods, goods_count, goods_type):
                    goods_buffer.append({"name": good.text, "count": good_count.text, "type": good_type.text, "url": "https://www.tender.pro"+good.get("href")})
                one_element["goods"] = goods_buffer
                #------------
                logger.debug(one_element)
                return one_element

    def get_urls(self, element, data_1, data_2):
        input_element_good_name = self.driver.find_element(By.ID, "good_name_id")
        input_element_data_1 = self.driver.find_element(By.ID, "date_1")
        input_element_data_2 = self.driver.find_element(By.ID, "date_2")
        input_element_good_name.send_keys(element)
        input_element_data_1.send_keys(data_1)
        input_element_data_2.send_keys(data_2)
        show_button = self.driver.find_element(By.ID, "view_tenders_list-submit")
        show_button.submit()

        while True:
            try:
                products_url = self.driver.find_elements(By.CLASS_NAME, "tender__name-wrapper")
                for i in products_url:
                    self.buffer.append(i.find_element(By.TAG_NAME, "a").get_attribute("href"))
                    self.table.append(self.get_tender_info(i.find_element(By.TAG_NAME, "a").get_attribute("href")))

                next_element = self.driver.find_element(By.CLASS_NAME, "pagination__link.pagination__link_next").get_attribute("href")
                self.driver.get(next_element)
            except:
                break

    def scrape_data(self, element, data_1, data_2):
        ret_data=self.table
        self.get_urls(element, data_1, data_2)
        df = pd.DataFrame(self.table)
        logger.info(df)
        df.to_csv(f"document_{self.formatted_date}.csv", sep=';', encoding='utf-8')
        time.sleep(11)
        return ret_data
        
    def quit_driver(self):
        self.driver.quit()


# if __name__ == "__main__":
#     tender_scraper = TenderScraper("/usr/local/bin/chromedriver",'/usr/bin/google-chrome')
#     tender_scraper.driver.get('https://www.tender.pro/api/tenders/list?sid=&company_id=&face_id=0&order=3&tender_id=&tender_name=&company_name=&good_name=&tender_type=90&tender_state=100&country=0&region=&basis=0&okved=&dateb=&datee=&dateb2=&datee2=')
#     tender_scraper.scrape_data("Арматура", "10.02.2024", "15.03.2024")
#     tender_scraper.quit_driver()
