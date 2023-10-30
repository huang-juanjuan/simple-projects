# -*- codeing = utf-8 -*-
# @Time:2020/11/11 17:51
# @Author:lcy
# @File: show1.py
# @Software:PyCharm
import xlrd
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
def show():
    text=xlrd.open_workbook(r'C:\Users\Hty\Desktop\trail\python\movieAnalysis\豆瓣电影TOP250.xls')
    sheet=text.sheet_by_name("豆瓣电影TOP250")
    type=[]
    for i in range(1,251):
        type.append(sheet.cell_value(i,4))
    n=[]
    for i in range(0,22):
        n.append(0)
    for i in range(0,250):
       if "犯罪" in type[i]:
           n[0]=n[0]+1
       if "剧情" in type[i]:
           n[1] = n[1] + 1
       if "爱情" in type[i]:
           n[2] = n[2] + 1
       if "同性" in type[i]:
           n[3] = n[3] + 1
       if "动作" in type[i]:
           n[4] = n[4] + 1
       if "灾难" in type[i]:
           n[5] = n[5] + 1
       if "科幻" in type[i]:
           n[6] = n[6] + 1
       if "动画" in type[i]:
           n[7] = n[7] + 1
       if "冒险" in type[i]:
           n[8] = n[8] + 1
       if "喜剧" in type[i]:
           n[9] = n[9] + 1
       if "悬疑" in type[i]:
           n[10] = n[10] + 1
       if "奇幻" in type[i]:
           n[11] = n[11] + 1
       if "传记" in type[i]:
           n[12] = n[12] + 1
       if "纪录片" in type[i]:
           n[13] = n[13] + 1
       if "家庭" in type[i]:
           n[14] = n[14] + 1
       if "历史" in type[i]:
           n[15] = n[15] + 1
       if "运动" in type[i]:
           n[16] = n[16] + 1
       if "儿童" in type[i]:
           n[17] = n[17] + 1
       if "惊悚" in type[i]:
           n[18] = n[18] + 1
       if "西部" in type[i]:
           n[19] = n[19] + 1
       if "战争" in type[i]:
           n[20] = n[20] + 1
       if "歌舞" in type[i]:
           n[21] = n[21] + 1
    level=250/22                                                       #平均值线
    name_list = ['犯罪','剧情','爱情','同性','动作','灾难','科幻','动画','冒险','喜剧','悬疑','奇幻','传记',
                 '纪录片','家庭','历史','运动','儿童','惊悚','西部','战争','歌舞']
    for i in range(0,21):
        for j in range(i+1,22):
            if n[i]<n[j]:
                n[i],n[j]=n[j],n[i]
                name_list[i],name_list[j]=name_list[j],name_list[i]
    plt.figure(figsize=(10,5))
    plt.ylim(0, 200)
    plt.bar(range(len(n)), n, color='red', tick_label=name_list,width=0.6)
    for i in range(len(n)):
        plt.text(i, n[i] + 0.01, format(n[i]), ha='center')
    plt.title("豆瓣TOP250各电影类型数量", fontsize=15)
    plt.hlines(level, -1, 22, linestyles='--', colors='#4472C4')
    plt.savefig('豆瓣电影TOP250各电影类型数量.png')
    plt.show()



if __name__ == '__main__':
    show()






