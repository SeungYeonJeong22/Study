import pandas as pd
import matplotlib.pyplot as plt

titanic_df = pd.read_csv("C:/Users/user/IndProj/IndStudy/Study/pandas/lab04_titanic/train.csv")

# print(titanic_df.info())

#생존자와 비생존자의 카운트 해보기

alive = titanic_df[titanic_df["Survived"]==1]
dead = titanic_df[titanic_df["Survived"]==0]

# print(len(alive) , '/' , len(titanic_df))
# print(len(dead) , '/' , len(titanic_df))

# plt.bar(["alive","dead"],height=[len(alive),len(dead)])
# plt.show()

#Scatter 이용 - 요금별 탑승자 시각화 하기
# plt.scatter(titanic_df["PassengerId"],titanic_df["Fare"])
# plt.xlabel("PassengerID")
# plt.ylabel("Fare")
# plt.show()

# 색상 분류 후 시각화 - 생존자는 초록색, 사망자는 빨간색
# plt.scatter(alive["PassengerId"],alive["Fare"],color='GREEN')
# plt.scatter(dead["PassengerId"],dead["Fare"],color='RED')
# plt.xlabel("PassengerID")
# plt.ylabel("Fare")
# plt.show()

#50$ 기준 탑승자 수
over_50 = titanic_df[titanic_df["Fare"]>=50]
under_50 = titanic_df[titanic_df["Fare"]<50]

# print(len(over_50),"/",len(titanic_df),   str(len(over_50)/len(titanic_df)*100)[:5] + '%')
# print(len(under_50),"/",len(titanic_df),  str(len(under_50)/len(titanic_df)*100)[:5]+ '%')

#생존자를 50 기준으로 나누기
alive_over_50 = over_50[over_50["Survived"]==1]
alive_under_50 = under_50[under_50["Survived"]==1]
# print(len(alive_over_50),'/',len(over_50),  str(len(alive_over_50)/len(over_50)*100)[:5] + '%')
# print(len(alive_under_50),'/',len(under_50),str(len(alive_under_50)/len(under_50)*100)[:5]+ '%')

plt.subplot(2,1,1)
plt.xlabel("$50미만 생존 비율")
plt.pie([len(alive_under_50),len(under_50)-len(alive_under_50)],colors=["GREEN","RED"],labels=("Alive","Dead"))

plt.subplot(2,1,2)
plt.xlabel("$50이상 생존 비율")
plt.pie([len(alive_over_50),len(over_50)-len(alive_over_50)],colors=["GREEN","RED"],labels=("Alive","Dead"))
plt.show()