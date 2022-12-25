import xlsxwriter
from tqdm import tqdm

from test import take_data_from_db

products = take_data_from_db()
last_products = []

# skuid, skuid_hb, name, id, market, price, brand, last_midified_date
#

for each in tqdm(products):
    try:
        product = dict()
        product['doc'] = each
        product['sku_id'] = each['sku_id']
        product['skuid_hb'] = each['skuid_hb']
        product['name'] = each['name']
        product['id'] = each['id']
        product['market'] = each['market']
        product['price'] = each['price']
        product['brand'] = each['brand']
        product['modified_date'] = each['modified_date']

        last_products.append(product)
    except Exception as error:
        print(error)

workbook = xlsxwriter.Workbook('Example3.xlsx')
worksheet = workbook.add_worksheet("My sheet")
row = 0
col = 0
worksheet.write(row, col, 'sku_id')
worksheet.write(row, col + 1, 'skuid_hb')
worksheet.write(row, col + 2, 'name')
worksheet.write(row, col + 3, 'id')
worksheet.write(row, col + 4, 'market')
worksheet.write(row, col + 5, 'price')
worksheet.write(row, col + 6, 'brand')
worksheet.write(row, col + 7, 'modified_date')
worksheet.write(row, col + 8, 'doc')

row = 1
for each_product in tqdm(last_products):
    col = 0
    # print(each_product['sku_id'])
    worksheet.write(row, col, str(each_product['sku_id']))
    worksheet.write(row, col + 1, str(each_product['skuid_hb']))
    worksheet.write(row, col + 2, str(each_product['name']))
    worksheet.write(row, col + 3, str(each_product['id']))
    worksheet.write(row, col + 4, str(each_product['market']))
    worksheet.write(row, col + 5, str(each_product['price']))
    worksheet.write(row, col + 6, str(each_product['brand']))
    worksheet.write(row, col + 7, str(each_product['modified_date']))
    worksheet.write(row, col + 8, str(each_product['doc']))
    row += 1
workbook.close()
