import pandas as pd

df=pd.read_csv("C:\\Users\\kalaimaran\\Downloads\\Employee.csv")

print(df.head())
print(df.tail())

## Handling Missing values
print(df.describe())
print(df.isnull().sum())
print(df.fillna(0))
print(df.isnull().any(axis=1))

## Data aggregating and Grouping
Grouped_mean=df.groupby('Age')['PaymentTier'].mean()
print(Grouped_mean)

## Merging and Joining DataFrame
# Create Sample Datafrome
df1=pd.DataFrame(
    {'key':['A','B','C'],'Value':['Apple','Banana','Cherry']}
)
df2=pd.DataFrame(
    {'Key':['A','B','C'],'Value':['App','Cry','Grape']}
)

print(df1)
print(df2)

## Merge DataFrame on the 'Key'
df1=pd.DataFrame(
    {'Key':['A','B','C'],'Value':['Apple','Banana','Cherry']}
)
df2=pd.DataFrame(
    {'Key':['A','B','C'],'Value':['App','Cry','Grape']}
)

print(pd.merge(df1,df2,on='Key',how='inner'))
print(pd.merge(df1,df2,on='Key',how='left'))
print(pd.merge(df1,df2,on='Key',how='outer'))
