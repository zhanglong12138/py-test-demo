import requests
from bs4 import BeautifulSoup
import json
import os

data = []

def getRandomUserAgent():
    return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
'537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'


def getData(page=1):
    thisPageList = []
    url = 'https://channels.weixin.qq.com/cgi-bin/mmfinderassistant-bin/live/get_live_history'
    

    headers = {
        # 'X-Wechat-Uin':'1205533462',
        # 'Finger-Print-Device-Id':'2c68b401d5fb77b4bed020bd65598123',
        'Cookie':'RK=oU0sYGAdY4; ptcz=153ffc4fe7dc5198581965bf897854f81e6797cfb8e3ddc756a567848e167a59; pgv_pvid=6973216496; pgv_pvi=6185591808; pac_uid=1_729099134; iip=0; eas_sid=b1C6z9j7F770B1s0M2s0U3f0N7; pgv_info=ssid=s9780054488; robloxqqcomrouteLine=index-pc; _clck=3213386079|1|fg0|0; sessionid=BgAA%2BnOcCQcq0IAJO1Dz56XRJFQGIvZ8caNddVxATgcHDZSuHToyYujJECZif9Pvkv2ZkAYJJMab4Vb9OTPd6eJy1TmIwaxg3jtY; wxuin=4123481487; _finder_fake_uin=AZ3WQyAadR9oDEcw%2BhMr4VUxuFKpixxV7Ljb8E6CrA2yJjhUOWqttGw%2Fhi5RjDmRY3aU58YAz7kOB%2BPCeyFacC88imn9ZlEj0FuraPSOGqRs9%2BDgIx3QJAlfv353aeKLd3Q5zIo%3D',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                        # '537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }

    #代理
    proxies = {
        # 'http': '222.66.202.6:80',
        'https': '222.66.202.6:80'
        # 'https': 'https://
    }

    payload = {
        "currentPage":page,
        "filterEndTime":1697731200,
        "filterStartTime":1610726400,
        "pageSize":10,
        "pluginSessionId":None,
        "rawKeyBuff":None,
        "reqScene":7,
        "reqType":2,
        "scene":7,
        "timestamp":1697785052170,
        "_log_finder_id":'v2_060000231003b20faec8c4e68919c7d2cd00ed33b07749a060c6b124365b9e1850de2f36f27a@finder',
        "_log_finder_uin":'',
    }

    # 发送HTTP GET请求获取页面内容
    useProxy = False
    if useProxy:
        response = requests.post(url,headers=headers,timeout=3500,proxies=proxies)
    else:
        # response = requests.post(url,headers=headers,payload=payload ,timeout=3500)
        #发个post请求
        response = requests.post(url,headers=headers,data=payload,timeout=3500)
        # response = requests.post(url,headers=headers,data=json.dumps(payload),timeout=3500)
    # 检查是否成功获取页面内容
    if response.status_code == 201:
        #解析json
        responseJson = response.json()
        
        return responseJson['data']['liveObjectList']
    #如果是200
    elif response.status_code == 200:
        #解析json
        responseJson = response.json()
        print(responseJson)
    else:
        print('无法访问页面')
        print(response.status_code)
    return thisPageList

#处理数据函数
def arrDeal(arr):
    for item in arr:
        liveStats = item['liveStats']
        liveStats["liveObjectId"] = item['liveObjectId']
        #直播市场 由秒转时分秒
        liveStats["liveDurationInSeconds"] = str(liveStats["liveDurationInSeconds"]//3600) + ':' + str(liveStats["liveDurationInSeconds"]%3600//60) + ':' + str(liveStats["liveDurationInSeconds"]%3600%60)
        data.append(liveStats)

#根据文件名和内容保存到文件
def save2file(filename):
    #映射关系
    relationship = {
        "currentOnlineCount":"当前在线人数",
        "eulerSingleJoin":"单场最高观看人数",
        "liveDurationInSeconds":"直播时长",
        "newFollowCount":"新增关注人数",
        "privateDomainUv":"私域流量",
        "totalAudienceCount":"累计观看人数",
        "totalAudiencesAvgSeconds":"人均观看时长",
        "totalCheerCount":"累计点赞数",
        "totalCommentCount":"累计评论数",
        "totalJoinliveCount":"累计进入直播间人数",
        "totalRewardNum":"累计打赏人数",
        "totalRewardTimes":"累计打赏次数",
    }
    
    #根据映射关系写入csv文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(','.join(relationship.values()) + '\n')
        for item in data:
            f.write(','.join([str(item[key]) for key in relationship.keys()]) + '\n')

     

def getFileName():
    #按时间戳转换为年月日和随机数生成文件名
    import time
    import random
    return time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000, 999999))            


#循环爬取 直到返回值为空数组
i = 1
while True:
    arr = getData(i)
    if len(arr) == 0:
        filename = getFileName() + '.csv'
        save2file(filename)
        break
    else:
        arrDeal(arr)
        i += 1



