import requests
import json
import time
import os

file1 = open("JSESSIONID.txt", "r")
input_JSESSIONID = file1.read()
file1.close()

file2 = open("iPlanetDirectoryPro.txt", "r")
input_iPlanetDirectoryPro = file2.read()
file2.close()

file3 = open("array.txt", "r")
input_array = file3.read()
file3.close()


script_path = __file__
script_name = os.path.basename(script_path)
script_name_without_extension = os.path.splitext(script_name)[0]
input_lessonid = script_name_without_extension


cookie = {
    "JSESSIONID": input_JSESSIONID,
    "array": input_array,
    "iPlanetDirectoryPro": input_iPlanetDirectoryPro,
}

header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "17",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Cookie": cookie,
    "Host": "jwgl.dhu.edu.cn",
    "Origin": "http://jwgl.dhu.edu.cn",
    "POST": "/dhu/selectcourse/accessJudge HTTP/1.1",
    "Referer": "http://jwgl.dhu.edu.cn/dhu/selectcourse/toSH",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}


def getLesson(lessonID):
    url = (
        "http://jwgl.dhu.edu.cn/dhu/selectcourse/scSubmit?cttId="
        + lessonID
        + "&needMaterial=false"
    )
    session = requests.Session()
    requests.headers = header
    response = session.post(url, cookies=cookie, timeout=(10, 20))
    print(response.text)
    if response.text.find("\"success\":true") != -1:
        return True


i = 0
flag = False
while not flag:
    print("目标课程：" + input_lessonid)
    print("!! 尝试第" + str(i + 1) + "次抢课")
    try:
        if getLesson(input_lessonid) == True:
            flag = True
            print("!! 抢课成功")
        else:
            print("!! 第" + str(i + 1) + "次抢课失败，继续尝试")
        time.sleep(2)
        i = i + 1
    except:
        print("!! 第" + str(i + 1) + "次抢课发生内部错误，继续尝试")
        i = i + 1
