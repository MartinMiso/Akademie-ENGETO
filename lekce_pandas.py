import pandas as pd

# data = pd.Series([10, 20, 30, 40], index = ["Test1", "Test2", "Test3", "Test4"])

# print(data)
# print(data["Test2"])
# print(data.mean())
# print(data > 25)
# print(data.sum())
# print(data.min())
# print(data.max())

df = pd.DataFrame({
    "Jméno": ["Jan", "Eva", "Petr"],
    "Status": ["Ok", "Ok", "Failed"],
    "Doba běhu": [2.3, 4.1, 1.8]
})

#print(df) # celé
#print(df["Status"]) # daný sloupec
#print(df.loc[1]) # daný index
#print(df.iloc[2]) # vrátí řádek podle pořadí
#print(df.loc[1, "Jméno"]) # podle indexu řádku a sloupce
#print(df.iloc[2, 1]) # konkrétní buňku podle řádku a sloupce

