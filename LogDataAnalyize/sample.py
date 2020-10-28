import pandas as pd

data_file = pd.read_csv("C:/Users/user/IndProj/IndStudy/LogDataAnalyize/KakaoTalk_20200729_1141_56_556_group_B.txt",delimiter = '\t')
print(data_file)
print(data_file.values[0])
