import pandas as pd
data={"Name":['ALi',"muhammad","express"],
      "age":[34,33,44],
      "City":["kpk","multan","balochistan"]
}
data["salary"]=[500,700,655]
df=pd.DataFrame(data)
print(df)


print(df['age'],mean())
print(df['age'],max())
print(df['age'],min())