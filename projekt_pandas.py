import pandas as pd

# df = pd.DataFrame({
#     "ID": [1, 2, 3, 4, 5, 2, 6],
#     "Jméno": ["LoginTest", "RegistrationTest", "SearchTest", "LogoutTest", "UploadTest", "RegistrationTest", "ProfileUpdateTest"],
#     "Status": ["Ok", "Failed", "Ok", "Failed", "Ok", "Failed", "Failed"],
#     "Doba běhu": [2.3, 4.1, 1.2, 3.5, 2.0, 4.1, 3.7],
#     "Chybová hláška": [None, "ValidationError", None, None, None, "ValidationError", None]
# })

# print(df)
# df.to_csv("test_data_new.csv", index=False, encoding="UTF-8")

df = pd.read_csv("test_data_new2.csv")

# print(df)
# print(df.head()) # vytiskne pouze prvních 5 řádků nebo do závorky číslo a vytiskne daný počet řádků
# print(df.info()) # ukáže typy atd.
# print(df.shape) # počet řádků a sloupců
# print(df.columns)
# print(df.dtypes)
# print(df.isnull().sum()) # ukáže nulové hodnoty a přidáním sum je to sečte a vypadá to lépe
# print(df[df["Chybová hláška"].isnull()]) # vypíše pouze ty řádky, kde není vyplněná hodnota

# df["Chybová hláška"] = df["Chybová hláška"].fillna("Neznámá chyba") # nahrazení nulových hodnot

# df.to_csv("test_data_new2.csv", index=False, encoding="utf-8")

# print(df.duplicated().sum())
# df = df.drop_duplicates()
# df.to_csv("test_data_new2.csv", index=False, encoding="utf-8")

# print(df["Status"].value_counts()) # vrátí součty podle sloupce
# print(df["Chybová hláška"].value_counts())

# print(df.groupby("Status")["Doba běhu"].mean()) # seskupý různé hodnoty ze sloupců mean dělá průměr

# print(df.groupby(["Status", "Jméno"]).size()) # seskupení s výskytem
print(df.describe())