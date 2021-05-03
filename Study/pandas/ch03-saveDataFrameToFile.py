import pandas as pd

friends = {
    {'name':'John','age':25,'job':'student'},
    {'name':'Jenny','age':30,'job':None},
    {'name':'Nate','age':35,'job':'teacher'}
}

df = pd.DataFrame(friends)
df = df[['name','age','job']]
print(df.head())

#데이터 프레임 액셀 파일 생성 default 값으로 index = True, header = True로 설정
df.to_csv('friends.csv',index=False,header=False)