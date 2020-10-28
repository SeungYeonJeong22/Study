import numpy as np
import pandas as pd


def sp(obj):
    print(obj)
    print('<-------------------->')


df_list_csv = pd.read_csv('../../pandas-master/data/friend_list.csv')
df_list_txt = pd.read_csv('../../pandas-master/data/friend_list.txt')
df_list_no_head_csv = pd.read_csv('../../pandas-master/data/friend_list_no_head.csv', header=None)
df_list_no_head_csv.columns = ['asd','fds','bvc']

df_list_tab_txt = pd.read_csv('../../pandas-master/data/friend_list_tab.txt', delimiter='\t')

sp(df_list_csv)
sp(df_list_csv.head(2))
sp(df_list_csv.tail(2))
sp(df_list_txt)
sp(df_list_no_head_csv)
sp(df_list_tab_txt)