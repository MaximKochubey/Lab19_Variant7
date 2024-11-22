import pandas as pd

df = pd.read_json('boys.json')

df['birth_date'] = pd.to_datetime(df['birth_date'], format='%Y-%m-%d')

series = pd.Series(df['birth_date'].values, index=df['name'])

series.to_json('dtm.json')

print("Дати народження успішно записано в dtm.json")

