from typing import Optional,List
from loguru import logger
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from tender_pro_linux import TenderScraper
from datetime import date
from pydantic import BaseModel
from pathlib import Path
from word_filter import TextFilter
import pandas as pd

class MyModel(BaseModel):
    filter: List[str] = [""]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["GET", "POST", "PUT", "DELETE"],
)

@app.get("/")
def root():
    return 

@app.post("/parse_tenderpro")
async def parse_tender_pro(element:str,date_1:str,date_2:str,filter:MyModel):
    logger.success(filter)
    tender_scraper = TenderScraper("/usr/local/bin/chromedriver-linux64/chromedriver",'/usr/bin/google-chrome')
    tender_scraper.driver.get('https://www.tender.pro/api/tenders/list?sid=&company_id=&face_id=0&order=3&tender_id=&tender_name=&company_name=&good_name=&tender_type=90&tender_state=100&country=0&region=&basis=0&okved=&dateb=&datee=&dateb2=&datee2=')
    result=tender_scraper.scrape_data(element, date_1, date_2)
    filter_instance = TextFilter(filter.filter)
    new_res=[]
    counter=0
    if filter.filter!=None:
        for index in result:
            names= [item["name"] for item in index["goods"]]
            logger.debug(len(names))
            filtered_texts = filter_instance.filter_texts(names)
            logger.warning(len(filtered_texts))
            if len(names)==len(filtered_texts):
                new_res.append(result[counter])
            counter+=1


    tender_scraper.quit_driver()
    logger.warning(len(new_res))
    return new_res


