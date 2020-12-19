# 接口测试：
#   接口文档；
#   构造接口消息并发送/接收服务端响应的工具：内置库httplib、urllib2、第三方库urllib3、requests、pyCurl

# 针对测试用例的第一步，发起一个创建课程的http请求消息

# python_requests文档：https://requests.readthedocs.io/zh_CN/latest/

import requests
from pprint import pprint

# 1.列出课程
res = requests.get(
    'http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20'
)

pprint(res.json())   # json格式的响应消息体
if res.status_code == 200:
    print("检查点status_code200，通过")
else:
    print("检查点status_code200，未通过")



# 2.添加课程
res2 = requests.post(
    'http://localhost/api/mgr/sq_mgr/',
    # 构造请求消息体
    data={
        "action": "add_course",
        "data": '''
            {
                "name":"初中化学",
                "desc":"初中化学课程",
                "display_idx":"4"
            }'''
    }  # 表单格式{}
)
retObj = res.json()
pprint(retObj)
if retObj["retCode"] == 0:
    print("检查点===>返回结果retCode为0，检查通过")
else:
    print("不通过")

