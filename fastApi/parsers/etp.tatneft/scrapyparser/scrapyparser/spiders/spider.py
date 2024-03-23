import json
import random
from pathlib import Path
from loguru import logger

from scrapy import Selector
import scrapy

class TatneftSpider(scrapy.Spider):
    name = "tatneft"
    
    def start_requests(self):
        urls = [
            "https://etp.tatneft.ru/pls/tzp/f?p=220:562:13418402918463::::P562_OPEN_MODE,GLB_NAV_ROOT_ID,GLB_NAV_ID:,12920020,12920020",
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
        trs = response.xpath("//tbody/tr")

        # Строки с товарами
        goods_table = trs[6].xpath("td")
        goods = goods_table.xpath("//td[@class=' u-tL']")
        logger.debug(goods)
        
        unique = []
        for good in goods:
            logger.debug(good.xpath("@headers").get())
            logger.debug(good.css("td::text").get())
            
            unique.append(good.xpath("@headers").get())
        logger.debug(list(set(unique)))
            