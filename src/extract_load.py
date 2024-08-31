# imports
import yfinance as yf
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

from pandas import DataFrame
from yfinance import Ticker
# pegar cotacao
def get_data(ticker_name, periodo='1mo', intervalo='1d') -> DataFrame:
    
    ticker: Ticker = yf.Ticker(ticker_name)
    
    dados: DataFrame = ticker.history(period=periodo, interval=intervalo)[['Close']]
    
    dados['ticker'] = ticker_name
    
    return dados

def get_all_data_commodities(comm_names: list[str]) -> DataFrame:
    return pd.concat([get_data(comm_name) for comm_name in comm_names])

if __name__ == "__main__":
    # Import variaveis de ambiente
    commodities = ['CL=F', 'GC=F', 'SI=F']
    
    data_comm: DataFrame = get_all_data_commodities(comm_names=commodities)
    
    print(data_comm)
        
# concaternar ativos

# Salvar no DW