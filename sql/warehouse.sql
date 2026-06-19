CREATE SCHEMA staging;
CREATE SCHEMA warehouse;

create table staging.exchange_rates(
base_code varchar(20),
currency_code varchar(20),
exchange_rate numeric(18,6),
last_update timestamp
);
SELECT * FROM public.exchange_rates LIMIT 10;