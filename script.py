import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')
staten_island = inventory.loc[:10]
product_request = staten_island['product_description']

seed_request = inventory[(inventory['location']=='Brooklyn')&(inventory['product_type']=='seeds')]
mylambda = lambda x: True if x>0 else False
inventory['in_stock'] = [mylambda(q) for q in inventory['quantity']]
inventory['total_value'] = inventory.price*inventory.quantity
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda,axis=1)
