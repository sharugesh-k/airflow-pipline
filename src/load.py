import transform 
import sqlalchemy as sa
import psycopg2 
import logging


def load_exchange_data():
    df=transform.transform_exchange_data()
    engine=sa.create_engine("postgresql+psycopg2://postgres:sharugesh@localhost:5432/warehouse")
    df.to_sql("exchange_rates",engine,if_exists="append",index=False)
    logging.basicConfig(level=logging.INFO)
    logging.info("Data loaded successfully")

load_exchange_data()