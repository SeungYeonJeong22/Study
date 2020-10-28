import pandas as pd
from collections import OrderedDict

friend_dict_list = {
    {'name':'John', 'age':25,'job':'student'},
    {'name':'Nate', 'age':30,'job':'teacher'}
}


friend_orderd_dict = OrderedDict(
    [
        ('job',['student','teacher']),
        ('name',['John','Nate']),
        ('age',['25','30'])
    ]
)

df = pd.DataFrame.from_dict(friend_orderd_dict)
print(df.head())
print()

print("<--------------------List-------------------->")
print()

friend_list = [
    ['John',20,'student'],
    ['Nate',30,'teacher']
]

column_name = ['name','age','job']
df = pd.DataFrame.from_records(friend_list,columns = column_name)
print(df.head())
print("-----------------------")

friend_list2 = [
    ['name',['John','Nate']],
    ['age',[20,30]],
    ['job',['student','teacher']]
]
df = pd.DataFrame.from_items(friend_list2)
print(df.head())