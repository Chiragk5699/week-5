import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df.to_csv("titanic.csv", index=False)

print("titanic.csv created successfully!")
