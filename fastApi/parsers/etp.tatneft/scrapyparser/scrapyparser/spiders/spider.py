import time
import json
import random
from pathlib import Path
from loguru import logger

from parsel import Selector
import scrapy
from scrapy.http import TextResponse 
from selenium import webdriver
from selenium.webdriver.common.by import By

class TatneftSpider(scrapy.Spider):
    name = "tatneft"
    
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920x1080')

        self.headers = []
        self.datasummary = []
        self.datasummary_items = []

        self.driver = webdriver.Chrome(options=options)

    def start_requests(self):
        urls = [
            "https://etp.tatneft.ru/pls/tzp/f?p=220:562:13246815075804::::P562_OPEN_MODE,GLB_NAV_ROOT_ID,GLB_NAV_ID:,12920020,12920020"
        ]

        path = Path.cwd().parent.parent.joinpath("agents.json")
        logger.debug(path)        

        with open(path, "r") as f:
            self.headers = json.load(f)
        header = {"User-Agent": self.headers[random.randrange(0, len(self.headers))]["user_agent"]}

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=header)
    
    def closed(self, reason):
        logger.debug(f'Closed, reason: {reason}')
        logger.debug(len(self.datasummary))
        logger.debug(len(self.datasummary_items))

    def parse(self, response):
        reached_end = True
        self.driver.get(response.url)
        self.driver.maximize_window()
        time.sleep(3)

        pages = []
        while reached_end:
            if len(pages) > 1:
                reached_end = False
            try:
                pages.append(self.driver.page_source)
                button = self.driver.find_elements(By.XPATH, "//*[@id='R25399004548800692_data_panel']/div[2]/ul/li[3]/button")
                if button:
                    button[0].click()
                    time.sleep(2)
                else:
                    reached_end = False
            except Exception as e:
                logger.error(e)

        for page in pages:
            urls_to_check = []

            selector = Selector(text=page)
            table = selector.xpath("//table[@class='a-IRR-table']/tbody")

            for tr in table.xpath('tr'):
                
                item = {}
                for td in tr.xpath('td'):
                    
                    url = td.xpath("a").xpath("@href").get()

                    if url:
                        detailed_url = "https://etp.tatneft.ru/pls/tzp/" + str(url)
                        item["DETAILED_URL"] = detailed_url

                        urls_to_check.append(detailed_url)

                    value = 0 
                    key = td.xpath('@headers').get()

                    if td.xpath('nobr/text()'):
                        value = td.xpath('nobr/text()').get()
                    else:
                        value = td.css("td::text").get()

                    item[f"{key}"] = value
                    
                self.datasummary.append(item)

            for url in urls_to_check:
                time.sleep(2.0)
                self.driver.get(url)
                page = self.driver.page_source

                items = []
                selector = Selector(text=page)
                everything = selector.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody")

                for table in everything.xpath("//table[@class='ReportTbl']"):
                    if ("Кол-во" and "Наименование" and "№" and "Замечание") in table.get():
                        for tr in table.xpath('tbody/tr'):
                            row = tr.xpath('td/text()').getall()
                            if row:
                                name = row[1]
                                number = row[2]
                                metrics = row[3]
                                mark = " "
                                if len(row) == 5:
                                    mark = row[4]
                                
                                current_item = {
                                    "name": name,
                                    "number": number,
                                    "metrics": metrics,
                                    "mark": mark
                                }

                                items.append(current_item)

                self.datasummary_items.append(
                    {
                        "url": response.url,
                        "items": items
                    }
                )
