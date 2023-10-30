from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt

# 创建正则表达式对象
findlink=re.compile(r'<a href="(.*?)">')
findname=re.compile(r'<span class="title">(.*?)</span>')
findgrade=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findnumber=re.compile(r'<span>(.*?)人评价</span>')
findabout=re.compile(r'<p class="">(.*?)</p>',re.S)

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist=getdata(baseurl)
    insertdata(datalist)

def insertdata(datalist):
    workbook=xlwt.Workbook(encoding="utf-8",style_compression=0)
    worksheet=workbook.add_sheet("豆瓣电影TOP250",cell_overwrite_ok=True)
    # tuple <=> const list
    col=("电影链接","电影名称","评分","评价人数","电影类型")
    for i in range(0,5):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        data=datalist[i]
        for j in range(0,5):
            if j==4:
                # 找最后一个 '\' 的下一位，'&nbsp;' 被转义为一个空格，所以是取下一位
                data[j]=data[j][data[j].rfind('/')+1:]
            worksheet.write(i+1,j,data[j])
    workbook.save("豆瓣电影TOP250.xls")


def getdata(baseurl):
    datalist = []
    for i in range(0,10):
        # "https://movie.douban.com/top250?start=" + "i" 为排名i的电影
        nowurl=baseurl+str(i*25)
        # 保存网页源码
        html=askurl(nowurl)
        soup = BeautifulSoup(html, "html.parser")
        # 寻找 div 控件，要求 class 为 “item”，即每个排名的电影的 item
        for item in soup.find_all('div',class_="item"):
            data=[]
            item=str(item)
            link=re.findall(findlink,item)[0]
            data.append(link)
            name=re.findall(findname,item)[0]
            data.append(name)
            grade =re.findall(findgrade,item)[0]
            data.append(grade)
            number =re.findall(findnumber,item)[0]
            data.append(number)
            about=re.findall(findabout,item)[0]
            data.append(about)
            datalist.append(data)
        for i in range(len(datalist)):
            print(datalist[i])
    return datalist

def askurl(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
    #用来伪装，告诉浏览器我们可以接收什么类型的数据。
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("UTF-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
if __name__ =="__main__":
    main()







