import json
import os
import psycopg2

# this is one way of inserting data into our database but not the best way if we are dealing with foreign keys, we can use fixtures instead

ingredients_data_path = os.path.join(os.path.dirname(__file__), "data/ingredients-data.json")

ingredients = json.load(open(ingredients_data_path))

conn = psycopg2.connect(host="localhost", database="djangodb", user="nehcobiy",  password=837737)

cur = conn.cursor()

for ingredient in ingredients:
    cur.execute("INSERT INTO learning_api_ingredient (category, name, price, flavour) VALUES (%s, %s, %s, %s)", (ingredient["category"], ingredient["name"], ingredient['price'], ingredient["flavour"]))


conn.commit()
cur.close()
conn.close()
