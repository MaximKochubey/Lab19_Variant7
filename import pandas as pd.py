import pandas as pd

df = pd.read_csv("masiv.csv", header=None)

row_sums = df.sum(axis=1)

with open("res.txt", "w") as f:
    for row_sum in row_sums:
        f.write(str(row_sum) + "\n")

print("Суми рядків записано в файл res.txt")
