#누가 어떤말을 가장 많이 했는지
#날짜별로 누가 얼마나 말했는지
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# import tensorflow as tf

# data_file = pd.read_csv("C:/Users/user/IndProj/IndStudy/LogDataAnalyize/KakaoTalk_20200729_1433_06_932_group_A.txt",header=None,error_bad_lines=False)
data_file = pd.read_csv("C:/Users/user/IndProj/IndStudy/LogDataAnalyize/KakaoTalk_20200729_1141_56_556_group_B.txt",delimiter = '\t',error_bad_lines=False)

chat_log = []
t_chat_log = []
#data_file은 DataFrame이고 DataFrame의 값의 각 인덱스는 ndArray이므로 ndArray의 불필요한 부분을 걸러내기 위해 임시 배열에 담아놓는다
for a in data_file.values:
    t_chat_log.append(a)

#ndArray의 0번 인덱스들(실질적 채팅 로그)만 걸러내기 위해
for a in t_chat_log:
    chat_log.append(a[0])

#채팅로그 파일의 인덱스 부분
tmp_name_list = str(data_file.keys())
member = {'승연':0}
#멤버 구분
tmp_name_Findx = tmp_name_list.find('님과')-1
tmp_name_Sindx = tmp_name_list.find('\'')+1
tmp_name_list = tmp_name_list[tmp_name_Sindx:tmp_name_Findx]
tmp_name_list = tmp_name_list.replace(',','').split(' ')
#멤버 초기화
for a in tmp_name_list:
    member[a] = 0

real = 0
injung = 0
zzzz = 0

for chat in chat_log:
    if chat.find('[') == 0:
        f_name = chat.find(']')+1
        t_nm = chat[:f_name]
        
        if t_nm in chat:
            if t_nm.strip('[]') in member:
                member[t_nm.strip('[]')] = member[t_nm.strip('[]')]+1

    if 'ㄹㅇ' in chat:
        real = real+1
    elif 'ㅇㅈ' in chat:
        injung = injung + 1
    elif 'ㅋㅋㅋㅋ' in chat:
        zzzz = zzzz + 1

plt1 = plt.subplot(1,2,1)
plt2 = plt.subplot(1,2,2)

plt.xlabel('CHAT')
# plt2.xlabel('Member')

members = {}

for _ in member.keys():
    if _ == '성재':
        members['seong'] = member['성재']
    elif _ == '재경':
        members['jae'] = member['재경']
    elif _ == '동후':
        members['dong'] = member['동후']
    elif _ == '윤환':
        members['yoon'] = member['윤환']
    elif _ == '승연':
        members['seungyeon'] = member['승연']

plt1.pie([real,injung,zzzz],colors=['BLUE','GREEN','RED'],labels=('real','injung','zzzz'))
plt2.pie(members.values(),colors=['BLUE','GREEN','RED','YELLOW','PINK'],labels=members.keys())

plt.show()

print(members)
sumChat = 0
for a in members.values():
    sumChat += a

print('sum : ',sumChat ,'\t avg : ',sumChat/len(member))
print("ㄹㅇ : ",real)
print("ㅇㅈ : ",injung)
print('ㅋㅋㅋㅋ : ',zzzz)
