#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from fastapi import Request, Depends, BackgroundTasks, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session


# from coronavirus.database import engine, SessionLocal, Base


from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


application = APIRouter()


application.mount('/static', StaticFiles(directory='./coronavirus/static'), name='static')
templates = Jinja2Templates(directory='./coronavirus/templates')


# Base.metadata.create_all(bind=engine)


@application.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "This is title"})  # {"request": request}是必须的


@application.get("/coronavirus")
async def coronavirus():
    """This is a simple tutorial"""
    return {"message": {"This is another route"}}


# class StockRequest(BaseModel):
#     symbol: str
#
#
# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# @application.get("/")
# def home(request: Request, forward_pe=None, dividend_yield=None, ma50=None, ma200=None, db: Session = Depends(get_db)):
#     """
#     displays the stock screener dashboard / homepage
#     :return:
#     """
#     stocks = db.query(Stock)
#
#     if forward_pe:
#         stocks = stocks.filter(Stock.forward_pe < forward_pe)
#
#     if dividend_yield:
#         stocks = stocks.filter(Stock.dividend_yield > dividend_yield)
#
#     if ma50:
#         stocks = stocks.filter(Stock.price > Stock.ma50)
#
#     if ma200:
#         stocks = stocks.filter(Stock.price > Stock.ma200)
#
#     return templates.TemplateResponse("home.html", {
#         "request": request,
#         "stocks": stocks
#     })
#
#
# def fetch_stock_data(id_: int):
#     """
#     fetch data from yahoo finance
#     :param id_:
#     :return:
#     """
#     db = SessionLocal()
#     stock = db.query(Stock).filter(Stock.id == id_).first()
#
#     yahoo_data = yf.Ticker(stock.symbol)
#
#     stock.ma50 = yahoo_data.info["fiftyDayAverage"]
#     stock.ma200 = yahoo_data.info["twoHundredDayAverage"]
#     stock.price = yahoo_data.info["previousClose"]
#     stock.forward_pe = yahoo_data.info["forwardPE"]
#     stock.forward_eps = yahoo_data.info["forwardEps"]
#     if yahoo_data.info["dividendYield"]:
#         stock.dividend_yield = yahoo_data.info["dividendYield"] * 100
#
#     db.add(stock)
#     db.commit()
#
#
# @application.post("/stock")
# async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
#     """
#     created a stock and stores it in the database
#     :return:
#     """
#     stock = Stock()
#     stock.symbol = stock_request.symbol
#
#     db.add(stock)
#     db.commit()
#
#     background_tasks.add_task(fetch_stock_data, stock.id)
#
#     return {
#         "code": "success",
#         "message": "stock created"
#     }
