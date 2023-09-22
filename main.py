import requests
import json
import time

file = open("token.txt", "r")
input_sessionid = file.read()
file.close()

# 在这里设置你想要抢的选课代码
input_lessonid = "267967"


cookie = {
    "JSESSIONID": input_sessionid,
    "array": "jwgl_03",
    "array": "jwgl_03",
    "array": "jwgl_03",
}


def getLesson(lessonID):
    url = (
        "http://jwgl.dhu.edu.cn/dhu/selectcourse/scSubmit?cttId="
        + lessonID
        + "&needMaterial=false"
    )
    session = requests.Session()
    response = session.post(url, cookies=cookie, timeout=(10, 20))
    print(response.text)
    if response.text.find("true") != -1:
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
