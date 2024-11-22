import pandas as pd  


filename_input = "masiv.csv"  
df = pd.read_csv(filename_input, header=None)  


row_sums = df.sum(axis=1)  

filename_output = "res.txt"  
with open(filename_output, "w") as f:
    for idx, value in enumerate(row_sums, start=1):  
        f.write(f"Рядок {idx}: сума = {value}\n")  

print("Суми рядків успішно записані у файл res.txt!")
