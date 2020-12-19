import unittest
import requests
import json
import jsonpath  #解析器

class MyTestCae(unittest.TestCase):

    def test_checklist1(self):
        # 请求url
        url = "http://39.98.136.157:5000/api/getbloodchecklist?cardnum=10987"
        # 使用requests.get请求数据
        res = requests.get(url)
        print(res.content)
        resjson = json.loads(res.content)
        print(resjson)
        # 断言
        result = jsonpath.jsonpath(resjson, "$.cardname")
        print(result)

        self.assertEqual("张一鸣", result)


if __name__ == "__main__":
    unittest.main()
