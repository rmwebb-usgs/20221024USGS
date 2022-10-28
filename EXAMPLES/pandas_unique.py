import pandas as pd

df = pd.read_table("../DATA/presidents.txt", delimiter=":")
df.index = range(1,len(df)+1)

print(df.head())
print()
parties = df.iloc[:,-1].value_counts()
print(parties)
# parties.plot(kind='bar')
print()
print(len(df.iloc[:,-1].unique()))
