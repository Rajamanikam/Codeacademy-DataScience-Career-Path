import pandas as pd
#Loading the inventory.csv into new dataframe called 'inventory'
inventory = pd.read_csv('inventory.csv')
# Inspecting only first 10 rows of inventory dataframe 
print(inventory.head(10))

staten_island = inventory[inventory.location == 'Staten Island']

print(type(staten_island))

product_request = staten_island['product_description']

print(product_request)

# Adding new column to find out what types of seeds are sold at the Brooklyn location
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

print(seed_request)

#Creating lambda function for determining the avalability status for each product in inventory
mylambda = lambda x: True if x > 0 else False

#Adding Column to show Product's Availabilty Status
inventory['in_stock'] = inventory.quantity.apply(mylambda)

print(inventory)

# Adding Column to know how valuable the current inventory is.
inventory['total_value'] = inventory.apply(lambda row: row['price'] * row['quantity'], axis=1)

print(inventory)

#Lambda Fuction for creating full description for each product
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

#Adding Column that has the complete description of each product.
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory)