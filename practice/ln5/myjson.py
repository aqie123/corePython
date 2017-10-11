# 如何读写json数据
'''
问题：本地音频post到Baidu语音识别服务器
服务器响应json字符串
python中如何读写json

解决：
json模块 loads,dumps 完成读写
App ID: 9586592

API Key: g0WG86oUwxZkcGGjlfgcNUbGhRuWZL0C

Secret Key: C3isHlwg3g3pHbV9xgtT1IEEwLyca0by
'''

# http get post 请求
import requests
import json

# 录音
'''
from Record import Record
record = Record(channels=1)
audioData = record.record(2)
'''


# 获取Token
'''
from secret import API_KEY, SECRET_KEY
authUrl = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY

response = requests.get(authUrl)
res = json.loads(response.content)
token = res['access_token']

print(token)
'''

# 语音识别
cuid = 'eat'
srvUrl = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token='+token
httpHeader = {
	'Content-type' : 'audio/wav; rate=8000',
}

response = requests.post(srvUrl,headers=httpHeader,data=audioData)
res = json.loads(response.content)
text = res['result'][0]

print('识别结果')
print(text)