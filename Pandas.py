import pandas as pd
## Series
data=[1,2,3,4,5,6]
series=pd.Series(data)
print(series)

## Series from dictionary
data={'A':'Kalai','B':'Krish','C':'Leo'}
data_dict=pd.Series(data)
print(data_dict)

#Series Index
data=[10,20,30,40]
index=['A','B','C','D']
Ind_ex=pd.Series(data,index=index)
print(Ind_ex)

##Dataframe (Create a DataFrame from a dict to list)
data={
    'Name':['Kalai','Krish','Leo'],
    'Age':[20,30,40],
    'Dept':['Mech','Civil','Cse']
}

df=pd.DataFrame(data)
print(df)

##Create a dataframe List of Dictionary
data=[
    {'Name':'Kalai','Age':20},
    {'Name':'Krish','Age':30},
    {'Name':'Leo','Age':40}
]
df=pd.DataFrame(data)
print(df)

## Accessing a specified Elememt
age=df.at[2,'Age']
print(age)

## Accessing a specified 'iat' Element
age1=df.iat[1,1]
print(age1)
