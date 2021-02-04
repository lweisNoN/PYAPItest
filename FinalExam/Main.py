#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from API import callApi
# 1. 打开测试文件 mock.data，这个代表测试数据
# 可以是本地的excel，也可以是网页上填写的json
with open('data.json', 'r') as f:
    data = json.load(f)

# 2. 测试获取结果

# 测试接口1，学生是否通过语文考试
chinese = data[0]
stu1ch = callApi(chinese['students'][0])
stu2ch = callApi(chinese['students'][1])

# 测试接口2，学生是否通过数学考试
math = data[1]
stu1en = callApi(math['students'][0])
stu2en = callApi(math['students'][1])

# 3. 写入结果文件
student1 = {}
student1['name'] = stu1ch[0]
student1['ch'] = stu1ch[1]
student1['en'] = stu1en[1]
student2 = {}
student2['name'] = stu2ch[0]
student2['ch'] = stu2ch[1]
student2['en'] = stu2en[1]
resArray = [student1, student2]
with open('result.json', 'w') as f:
        json.dump(resArray, f)

# 4. 保存结果文件
