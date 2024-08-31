# imports
import yfinance as yf
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

from pandas import DataFrame
from yfinance import Ticker
from sqlalchemy import Engine
# pegar cotacao
def get_data(ticker_name, periodo='5d', intervalo='1d') -> DataFrame:
    
    ticker: Ticker = yf.Ticker(ticker_name)
    
    dados: DataFrame = ticker.history(period=periodo, interval=intervalo)[['Close']]
    
    dados['ticker'] = ticker_name
    
    return dados

def get_all_data_commodities(comm_names: list[str]) -> DataFrame:
    return pd.concat([get_data(comm_name) for comm_name in comm_names])

def save_db(df: DataFrame, schema: str, engine: Engine):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)
    
    return

if __name__ == "__main__":
    # Import variaveis de ambiente
    
    load_dotenv('.env')
    
    DB_HOST = os.getenv("DB_HOST_PROD")
    DB_PORT = os.getenv("DB_PORT_PROD")
    DB_NAME = os.getenv("DB_NAME_PROD")
    DB_USER = os.getenv("DB_USER_PROD")
    DB_PASS = os.getenv("DB_PASS_PROD")
    DB_SCHEMA = os.getenv("DB_SCHEMA_PROD")
    
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)
    
    commodities = ['CL=F', 'GC=F', 'SI=F']
    
    schema = 'public'
    
    data_comm: DataFrame = get_all_data_commodities(comm_names=commodities)
    
    save_db(data_comm, schema, engine)
    
    
        
# concaternar ativos

# Salvar no DW