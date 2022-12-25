import json
import psycopg2
import requests
from tqdm import tqdm

conn_new = psycopg2.connect(database="narmoni", user='postgres', password='4rf#dfer53RF4#@',
                            host='172.31.24.65', port='5432')

cursor = conn_new.cursor()
HERO_API_ADDRESS = 'http://172.31.94.152:5000/data/dynamic/'


def get_data_from_api(data):
    market = data[1]
    stock_id = f"/{data[0]}"
    product_address = HERO_API_ADDRESS + market + stock_id
    # print(product_address)
    try:
        res = json.loads(requests.get(product_address).content)
        return res
    except Exception as e:
        print(e)
        pass


def take_data_from_db():
    dynamic_price_data = []
    query_sting = f"select stock_id , market  from dynamic.product"
    cursor.execute(query_sting)
    cursors = cursor.fetchall()

    for index, each in enumerate(tqdm(cursors)):
        try:
            product = get_data_from_api(each)
            dynamic_price_data.append(product)
        except Exception as error:
            print(error)
            pass
    return dynamic_price_data
