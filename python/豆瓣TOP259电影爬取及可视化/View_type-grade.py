# -*- coding: <encoding name> -*- :
# -*- coding: utf-8 -*-
import xlrd
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
def show():
    text=xlrd.open_workbook(r'C:\Users\Hty\Desktop\trail\python\movieAnalysis\豆瓣电影TOP250.xls')
    sheet=text.sheet_by_name("豆瓣电影TOP250")
    type=[]
    grade=[]
    for i in range(1,251):
        type.append(sheet.cell_value(i,4))
        grade.append(float(sheet.cell_value(i,2)))
    n=[]
    ave=[]
    for i in range(0,22):
        n.append(0)
        ave.append(0)
    for i in range(0,250):
       if "犯罪" in type[i]:
           n[0]=n[0]+1
           ave[0]=ave[0]+grade[i]
       if "剧情" in type[i]:
           n[1] = n[1] + 1
           ave[1] = ave[1] + grade[i]
       if "爱情" in type[i]:
           n[2] = n[2] + 1
           ave[2] = ave[2] + grade[i]
       if "同性" in type[i]:
           n[3] = n[3] + 1
           ave[3] = ave[3] + grade[i]
       if "动作" in type[i]:
           n[4] = n[4] + 1
           ave[4] = ave[4] + grade[i]
       if "灾难" in type[i]:
           n[5] = n[5] + 1
           ave[5] = ave[5] + grade[i]
       if "科幻" in type[i]:
           n[6] = n[6] + 1
           ave[6] = ave[6] + grade[i]
       if "动画" in type[i]:
           n[7] = n[7] + 1
           ave[7] = ave[7] + grade[i]
       if "冒险" in type[i]:
           n[8] = n[8] + 1
           ave[8] = ave[8] + grade[i]
       if "喜剧" in type[i]:
           n[9] = n[9] + 1
           ave[9] = ave[9] + grade[i]
       if "悬疑" in type[i]:
           n[10] = n[10] + 1
           ave[10] = ave[10] + grade[i]
       if "奇幻" in type[i]:
           n[11] = n[11] + 1
           ave[11] = ave[11] + grade[i]
       if "传记" in type[i]:
           n[12] = n[12] + 1
           ave[12] = ave[12] + grade[i]
       if "纪录片" in type[i]:
           n[13] = n[13] + 1
           ave[13] = ave[13] + grade[i]
       if "家庭" in type[i]:
           n[14] = n[14] + 1
           ave[14] = ave[14] + grade[i]
       if "历史" in type[i]:
           n[15] = n[15] + 1
           ave[15] = ave[15] + grade[i]
       if "运动" in type[i]:
           n[16] = n[16] + 1
           ave[16] = ave[16] + grade[i]
       if "儿童" in type[i]:
           n[17] = n[17] + 1
           ave[17] = ave[17] + grade[i]
       if "惊悚" in type[i]:
           n[18] = n[18] + 1
           ave[18] = ave[18] + grade[i]
       if "西部" in type[i]:
           n[19] = n[19] + 1
           ave[19] = ave[19] + grade[i]
       if "战争" in type[i]:
           n[20] = n[20] + 1
           ave[20] = ave[20] + grade[i]
       if "歌舞" in type[i]:
           n[21] = n[21] + 1
           ave[21] = ave[21] + grade[i]
    ave_list=[]
    name_list = ["犯罪", "剧情", "爱情", "同性", "动作", "灾难", "科幻", "动画", "冒险", "喜剧","悬疑",
                 "奇幻", "传记", "纪录片", "家庭", "历史", "运动","儿童", "惊悚", "西部", "战争", "歌舞"]
    level=0
    for i in range(0,22):
        if n[i]==0:
            continue
        ave[i]=ave[i]/n[i]
        level=level+ave[i]
        ave_list.append(ave[i])
    # bubble sort
    for i in range(0,21):
        for j in range(0,21-i):
            if ave_list[j]<ave_list[j+1]:
                ave_list[j],ave_list[j+1]=ave_list[j+1],ave_list[j]
                name_list[j],name_list[j+1]=name_list[j+1],name_list[j]
    # average grade
    level=level/22
    plt.figure(figsize=(10,5))
    plt.ylim(8.6, 9.3)
    plt.bar(range(len(ave_list)), ave_list, color='blue', tick_label=name_list,width=0.6)
    for i in range(len(ave_list)):
        plt.text(i, ave_list[i] + 0.01, '{:.2f}'.format(ave_list[i]), ha='center')
    plt.title("豆瓣TOP250各类型电影平均评分",fontsize=15)
    plt.hlines(level, -1, 22, linestyles='--', colors='#4472C4')
    plt.savefig('豆瓣电影TOP250各电影类型均分.png')
    plt.show()



if __name__ == '__main__':
    show()