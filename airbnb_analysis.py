import pandas as pd

# 讀取剛上傳的 CSV 檔案
df = pd.read_csv('airbnb_boston.csv')

# 顯示前五筆資料
df.head()

# 基本資料檢視
print("Data shape:", df.shape)
print("\nData info:")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nBasic statistics of numerical columns:")
print(df.describe())