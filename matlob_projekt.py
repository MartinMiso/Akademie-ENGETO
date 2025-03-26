import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


df = pd.read_csv("test_data_new2.csv")

# df["Status"].value_counts().plot(kind="bar", title="Můj super graf")

# plt.xlabel("Status")
# plt.ylabel("Počet testů")
# plt.tight_layout()
# plt.show()


# df["Doba běhu"].plot(kind="hist", bins=5, title="Můj super graf")
# plt.xlabel("Doba běhu (s)")
# plt.tight_layout()
# plt.show()

df.to_excel("report_data.xlsx", index=False)
nazev = (f"test_report_{datetime.now().strftime('%d-%m-%Y')}.xlsx")
df.to_excel(nazev, index=False)