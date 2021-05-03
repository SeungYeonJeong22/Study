import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('C:/Users/user/IndProj/IndStudy/Study/pandas/lab04_titanic/train.csv')

alive = titanic_df[titanic_df["Survived"]==1]
dead = titanic_df[titanic_df["Survived"]==0]

print(len(alive),'/',len(titanic_df))
print(len(dead),'/',len(titanic_df))

#50$ 기준
over_50 = alive[alive["Fare"]>=50]
under_50 = alive[alive["Fare"]<50]

print(len(over_50),'/',len(alive))
print(len(under_50),'/',len(alive))

# plt.bar(['alive','dead'],height=[len(alive),len(dead)])
# plt.xlabel('Passenger')
# plt.ylabel('Population')

plt.scatter(alive["PassengerId"],alive["Fare"],color = 'GREEN')
plt.scatter(dead["PassengerId"],dead["Fare"],color = 'RED')
plt.xlabel("PassengerId")
plt.ylabel("Fare")
plt.show()
