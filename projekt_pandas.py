import pandas as pd

df = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5, 2, 6],
    "Jméno": ["LoginTest", "RegistrationTest", "SearchTest", "LogoutTest", "UploadTest", "RegistrationTest", "ProfileUpdateTest"],
    "Status": ["Ok", "Failed", "Ok", "Failed", "Ok", "Failed", "Failed"],
    "Doba běhu": [2.3, 4.1, 1.2, 3.5, 2.0, 4.1, 3.7],
    "Chybová hláška": [None, "ValidationError", None, None, None, "ValidationError", None]
})

print(df)

df.to_csv("test_data_new.csv", index=False, encoding="UTF-8")