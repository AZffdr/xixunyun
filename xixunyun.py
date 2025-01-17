import requests
import json
import os

# 配置开始 
user = os.environ["USER"]
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
data = {
  "account":account,
  "password":password,
  "school_id":school_id,
  "longitude":longitude,
  "latitude":latitude,
  "address_name":os.environ["ADDRESS_NAME"] 
}
headers = {'Content-Type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

response = requests.post(url='https://api.xixunyun.com/login/api?from=app&version=5.1.1&platform=android', headers=headers, data=data)
if response.status_code==200:
  re = requests.get(url='https://api.xixunyun.com/signin_rsa?token="b1b0be25325e42429f468fb0790318cd"&from=app&version=5.1.1&platform=android&entrance_year=0&graduate_year=0&school_id='+school_id, headers=headers, cookies=response.cookies)
print(response.json()["data"])

SCKEY=os.environ["SCKEY"]
if len(SCKEY) >= 1:
  url = 'https://sctapi.ftqq.com/'+SCKEY+'.send'
  requests.post(url, data={"title": "习讯云签到提醒", "desp":'成功'})
