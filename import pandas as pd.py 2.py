import pandas as pd

boys = pd.read_json("boys.json")

print(boys.columns)

boys['birthdate'] = pd.to_datetime(boys['birthdate'])

print(boys.head())
