import time
import json
import random
from pathlib import Path
from loguru import logger

import scrapy

class TatneftSpider(scrapy.Spider):
    name = "tatneft"
    
    def start_requests(self):
        urls = [
            "https://etp.tatneft.ru/pls/tzp/f?p=220:562:13246815075804::::P562_OPEN_MODE,GLB_NAV_ROOT_ID,GLB_NAV_ID:,12920020,12920020"
        ]
        self.headers = []

        path = Path.cwd().parent.parent.joinpath("agents.json")
        logger.debug(path)        

        with open(path, "r") as f:
            self.headers = json.load(f)
        header = {"User-Agent": self.headers[random.randrange(0, len(self.headers))]["user_agent"]}

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=header)

    def parse(self, response):
        self.datasummary = []

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

        logger.debug(self.datasummary)

        for url in urls_to_check:
            header = {"User-Agent": self.headers[random.randrange(0, len(self.headers))]["user_agent"]}
            yield scrapy.Request(url, callback=self.detailed_parse, headers=header)

    def detailed_parse(self, response):
        time.sleep(0.2)
        first_table = response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td")

        index = 1

        everything = response.xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody")
        for table in everything.xpath("//table[@class='ReportTbl']"):
            if ("Кол-во" and "Наименование" and "№" and "Замечание") in table.get():
                logger.debug('Goods here')
                for tr in table.xpath('tbody/tr'):
                    logger.debug(tr.xpath('td').getall())