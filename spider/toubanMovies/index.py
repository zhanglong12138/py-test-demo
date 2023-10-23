import requests
from bs4 import BeautifulSoup
import json

movieCache = []

def getRandomUserAgent():
    # 随机获取一个浏览器头部信息
    # 从文件中读取浏览器头部信息
    with open('user_agents.txt', 'r') as f:
        user_agents = f.readlines()
    # 随机选择一个浏览器头部信息
    import random
    user_agent = random.choice(user_agents).replace('\n', '')
    return user_agent


def getDouBanTop250(page=1):
    thisPageList = []
    url = f'https://movie.douban.com/top250?start={(page-1)*25}&filter='
    # 豆瓣电影列表的URL
    # 构造随机浏览器信息headers
    # headers = getRandomUserAgent()
    # print(headers)
    # return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/'
                        '537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.37'
    }

    #代理
    proxies = {
        # 'http': '222.66.202.6:80',
        'https': '222.66.202.6:80'
        # 'https': 'https://
    }

    # 发送HTTP GET请求获取页面内容
    useProxy = False
    if useProxy:
        response = requests.get(url,headers=headers,timeout=3500,proxies=proxies)
    else:
        response = requests.get(url,headers=headers,timeout=3500)
    # 检查是否成功获取页面内容
    if response.status_code == 200:
        # 使用BeautifulSoup解析页面
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取电影信息
        movie_list = soup.find_all('div', class_='info')
        # print(movie_list)
        for movie in movie_list:
            # 电影标题
            title = movie.find('span', class_='title').get_text()
            # 电影评分
            rating = movie.find('span', class_='rating_num').get_text()
            # 电影评价人数
            num_ratings = movie.find('div', class_='star').find_all('span')[3].get_text().strip('人评价')
            # 导演和主演信息
            director_and_actors = movie.find('p', class_='').get_text().strip().split('\n')
            director = director_and_actors[0].strip()
            director = director.replace("\xa0", " ")
            actors = ', '.join(actor.strip() for actor in director_and_actors[1:])
            actors = actors.replace("\xa0", " ")
            thisPageList.append({
                'title': title,
                'rating': rating,
                'num_ratings': num_ratings,
                'director': director,
                'actors': actors
            })
        #反馈第N页爬取成功
        print(f'第{page}页爬取成功')
        dir = 'cache'
        #如果不存在目录
        import os
        if not os.path.exists(dir):
            #创建目录
            os.makedirs(dir)
        filename = f'{dir}/movie{page}.json'
        #写入第N页数据到本地文件 json格式
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(thisPageList, f, ensure_ascii=False, indent=4)
    else:
        print('无法访问页面')
        print(response.status_code)
    return thisPageList

for i in range(1, 11):
    movieCache.extend(getDouBanTop250(i))

# #储存为json格式的文件
# with open('movie.json', 'w', encoding='utf-8') as f:
#     json.dump(movieCache, f, ensure_ascii=False, indent=4)
