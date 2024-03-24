from loguru import logger
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from tenderpor_class_parser import TenderScraper
from datetime import date

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
async def parse_tender_pro(element:str,date_1:str,date_2:str):
    tender_scraper = TenderScraper('drivers\chromedriver.exe', 'chrome-win64\chrome.exe')
    tender_scraper.driver.get('https://www.tender.pro/api/tenders/list?sid=&company_id=&face_id=0&order=3&tender_id=&tender_name=&company_name=&good_name=&tender_type=90&tender_state=100&country=0&region=&basis=0&okved=&dateb=&datee=&dateb2=&datee2=')
    result=tender_scraper.scrape_data(element, date_1, date_2)
    tender_scraper.quit_driver()
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="26.204.194.141", port=8080)

