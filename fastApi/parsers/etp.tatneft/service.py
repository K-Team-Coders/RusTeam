from loguru import logger
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

process = CrawlerProcess(get_project_settings())

@app.post("/parse_tatneft")
def parse_tender_pro():
    process.crawl("tatneft")
    process.start() 

