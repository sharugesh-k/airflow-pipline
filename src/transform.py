import pandas as pd
from extract import extract


def transform_exchange_data():

    data = extract()

    rates = data["conversion_rates"]

    rows = []

    for currency, rate in rates.items():

        rows.append(
            {
                "base_code": data["base_code"],
                "currency_code": currency,
                "exchange_rate": rate,
                "last_update": data["time_last_update_utc"]
            }
        )

    df = pd.DataFrame(rows)

    return df


if __name__ == "__main__":
    print(transform_exchange_data().head())