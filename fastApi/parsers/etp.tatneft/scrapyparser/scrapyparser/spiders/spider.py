import json
import random
from pathlib import Path
from loguru import logger

from scrapy import Selector, Request
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

    def detailed_parse(self, response):
        logger.debug("Here")
        logger.debug(response.text)

    def parse(self, response):
        datasummary = []

        source = response.url
        logger.debug(source)

        table = response.xpath("//table[@class='a-IRR-table']")
        for tr in table.xpath('tr'):
            item = {}
            for td in tr.xpath('td'):
                
                url = td.xpath("a").xpath("@href").get()

                if url:
                    resp = response.follow(url)
                    self.detailed_parse(resp)

                item[f"{td.xpath('@headers').get()}"] = td.css("td::text").get()
            datasummary.append(item)

        logger.debug(datasummary)

        # # Строки с товарами
        # goods_table = trs[6].xpath("td")
        # goods = goods_table.xpath("//td[@class=' u-tL']")
        # logger.debug(goods)
        
        # for good in goods:
        #     logger.debug(good.xpath("@headers").get())
        #     logger.debug(good.css("td::text").get())
            
        #     unique.append(good.xpath("@headers").get())
        # logger.debug(list(set(unique)))
            