# coding:utf-8
import requests

# 指定访问的接口url
url = "http://localhost:8080/interfaceTest/login"
# 接口传入的参数
para = {
    "loginName": "mts",
    "pwd": "123456"
}  # 字典类型
# 发送get请求，默认返回一个response
res = requests.get(url, params=para)
print(res)
# 获取响应文本内容
print(res.text)
print(res.content)
print(type(res.text))  # string
