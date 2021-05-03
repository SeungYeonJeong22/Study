#계절에 따른 대기오염 현황
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = 'C:/Users/user/IndProj/IndStudy/Study/DataFile/Pollution/2018Pollution.CSV'
dataF = pd.read_csv(file_path)

print(dataF.info())
print(dataF.head(10))

