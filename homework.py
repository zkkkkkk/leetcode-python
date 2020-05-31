from bs4 import BeautifulSoup
import requests
import re
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': ua}

def getWordCloud(data):
    for k,v in data.items():
        tempwordcloud = WordCloud(font_path="C:\Windows\Fonts\simfang.ttf", width=2000,height=1500).generate(" ".join(jieba.cut("。".join(v))))
        plt.title(k + " wordcloud graph")
        plt.imshow(tempwordcloud, interpolation="bilinear", )
        plt.axis("off")
        plt.show()

def getTitleAndDate(url):
    '''
    输入url,返回url里所有新闻的标题和完整日期
    [
      ['2019.12.26', '教育部党组书记、部长陈宝生来西南财经大学调研指导  强调新时代要办“有灵魂、有情怀、有气度、有眼光、有激情”的社会主义大学'],
      ['2019.12.28', '中国共产党西南财经大学第十三届代表大会第二次会议举行']
    ]
    :return:
    '''
    req = requests.get(url, headers=headers)
    req.encoding = ('utf-8')
    content = req.text
    bsInstance = BeautifulSoup(content, 'html.parser')
    whloeNewsList = bsInstance.find_all('ul', class_='whitenewslist clearfix')
    actualNewsList = whloeNewsList[0].find_all('li')
    result = []
    for singleNews in actualNewsList:

        result.append([re.search('.*(?=\\.)', singleNews.span.i.string).group(), singleNews.a.attrs['title']])
    return result


def getNeedPageList(pageNum):
    '''
    前端不知道怎么怎么搞的，限制新闻页数；研究这个没必要吧，我们手动限制读多少页就可以了。正常看起来是25个页面加上首页。
    返回一个url的list
    :param pageNum:
    :return:
    '''
    url_list = []
    url_list.append("https://news.swufe.edu.cn/zhxw.htm") #首页
    otherPageBaseUrl = "https://news.swufe.edu.cn/zhxw/{index}.htm" #其他页面
    for i in range(1, pageNum+1):
        url_list.append(otherPageBaseUrl.format(index=i))
    return url_list

def aggrMonthAndNews(data):
    '''
    汇总所有页面里的[年月、标题]，这种格式的数据进行处理。按照月份划分
    返回{年月:[标题list]}这种格式的数据
    :param data:
    :return:
    '''
    resultDict = {}
    for singleNews in data:
        # print("log entry",resultDict, singleNews, sep='\t')
        if singleNews[0] in resultDict.keys():
            # print("log append", singleNews[0], resultDict[singleNews[0]], sep='\t')
            resultDict[singleNews[0]].append(singleNews[1])
        else:
            resultDict[singleNews[0]] = [singleNews[1]]
    return resultDict  

urlList = getNeedPageList(25)
rawData = []
for url in urlList:
    rawData.extend(getTitleAndDate(url))
aggrData = aggrMonthAndNews(rawData)
getWordCloud(aggrData)


