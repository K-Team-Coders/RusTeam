import time
import json
import random
from pathlib import Path
from loguru import logger

import scrapy
from scrapy_selenium import SeleniumRequest

class TatneftSpider(scrapy.Spider):
    name = "tatneft"
    
    def __init__(self):
        self.headers = []
        self.datasummary = []
        self.datasummary_items = []

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
            yield SeleniumRequest(url=url, callback=self.parse, headers=header)
    
    def closed(self, reason):
        logger.debug(f'Closed, reason: {reason}')
        logger.debug(len(self.datasummary))
        logger.debug(len(self.datasummary_items))

    def parse(self, response):
        source = response.url
        logger.debug(source)

        urls_to_check = []

        table = response.xpath("//table[@class='a-IRR-table']")
        for tr in table.xpath('tr'):
            item = {}
            for td in tr.xpath('td'):
                
                url = td.xpath("a").xpath("@href").get()

                if url:
                    detailed_url = response.follow(url=url).url
                    item["DETAILED_URL"] = detailed_url

                    urls_to_check.append(detailed_url)

                item[f"{td.xpath('@headers').get()}"] = td.css("td::text").get()
        
            self.datasummary.append(item)

        div = response.xpath("//div[@class='a-IRR-paginationWrap a-IRR-paginationWrap--bottom']")
        logger.debug(div.xpath('//button[@class="a-Button a-IRR-button a-IRR-button--pagination"]').get())
        urls_to_check = []


        for url in urls_to_check:
            header = {"User-Agent": self.headers[random.randrange(0, len(self.headers))]["user_agent"]}
            yield scrapy.Request(url, callback=self.detailed_parse, headers=header)

    def detailed_parse(self, response):
        time.sleep(0.2)
        first_table = response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td")

        items = []

        everything = response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody")
        for table in everything.xpath("//table[@class='ReportTbl']"):
            if ("Кол-во" and "Наименование" and "№" and "Замечание") in table.get():
                for tr in table.xpath('tbody/tr'):
                    row = tr.xpath('td/text()').getall()

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
