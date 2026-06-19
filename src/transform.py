import pandas as pd
import extract 


def transform_exchange_data():
    data=extract.data_exchange
    df=pd.DataFrame(data)
    rates = data["conversion_rates"]

    rows = []

    for currency, rate in rates.items():
        rows.append({
            "base_code": data["base_code"],
            "currency_code": currency,
            "exchange_rate": rate,
            "last_update": data["time_last_update_utc"]
        })

    df = pd.DataFrame(rows)

    print(df.head())
    return df

transform_exchange_data()