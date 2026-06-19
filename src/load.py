import sqlalchemy as sa
import logging

from transform import transform_exchange_data


def load_exchange_data():

    df = transform_exchange_data()

    engine = sa.create_engine(
        "postgresql+psycopg2://postgres:sharugesh@localhost:5432/warehouse"
    )

    with engine.begin() as connection:
        df.to_sql(
            "exchange_rates",
            connection,
            if_exists="append",
            index=False
        )

    logging.info("Data loaded successfully")


if __name__ == "__main__":
    load_exchange_data()