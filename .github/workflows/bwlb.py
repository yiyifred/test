import requests
import json
import time

headers= {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM3OTU1MjUsImlhdCI6MTcxNjAxOTUyNSwidXNlcl9pZCI6IjIzMTAxIn0.UKz2mYYrHAt6VBLjNW7AHq7h6PqDDU4latbABT01v-I",
    "Content-Type": "application/json",
    "x-user-id":"23101",
    "Host": "api-lbsns.feiyu.com",
    "Connection": "keep-alive",
    "x-wechat-version": "3.9.7",
    "x-sdk-version": "3.0.2",
    "x-app-version": "1.1.7",
    "x-device-type": "unknown",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM3OTU1MjUsImlhdCI6MTcxNjAxOTUyNSwidXNlcl9pZCI6IjIzMTAxIn0.UKz2mYYrHAt6VBLjNW7AHq7h6PqDDU4latbABT01v-I",
    "x-game-id": "1",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "x-env-version": "release",
    "xweb_xhr": "1",
    "x-content-version": "5"
}
headers2={
"Host": "api-lbsns.feiyu.com",
"Connection": "keep-alive",
"Content-Length": "37",
"x-wechat-version": "3.9.7",
"x-sdk-version": "3.0.2",
"x-app-version": "1.1.7",
"x-device-type": "unknown",
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM3OTU1MjUsImlhdCI6MTcxNjAxOTUyNSwidXNlcl9pZCI6IjIzMTAxIn0.UKz2mYYrHAt6VBLjNW7AHq7h6PqDDU4latbABT01v-I",
"x-game-id": "1",
"Content-Type": "application/json",
"Accept": "application/json, text/plain, */*",
"x-env-version": "release",
"xweb_xhr": "1",
"x-content-version": "5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461",
"x-user-uuid": "omfyR63k0YTDd8pMVizIM4bJ_aPs",
"x-user-id": "23101",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://servicewechat.com/wx67dc79a7512444ed/21/page-frame.html",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9"
}
data={"\"other_id\"":"23101"}
data2={"app_id":1,"user_game_role_id":1096}
data3={"app_id":1,"user_game_role_id":1097}
requests.request("post","https://api-lbsns.feiyu.com/v1/user/gameDefaultRoleEdit",headers=headers2,json=data2)
re = requests.request("post","https://api-lbsns.feiyu.com/v1/user/gameDefaultRoleList",headers=headers,json=data)
rabbit=re.text
rabbit=json.loads(rabbit)
id=rabbit["data"]["list"][0]["game_role_id"]
name=rabbit["data"]["list"][0]["game_role_name"]
channel=rabbit["data"]["list"][0]["game_channel_name"]
关卡挑战=rabbit["data"]["list"][0]["stage_pass"]
所有关卡=rabbit["data"]["list"][0]["stage_count"]
金萝卜=rabbit["data"]["list"][0]["gold_carrot"]
全清=rabbit["data"]["list"][0]["clear"]
people1=(f"ID：{id}，用户名：{name}，渠道：{channel}，关卡挑战：{关卡挑战}/{所有关卡}，金萝卜：{金萝卜}/{所有关卡}，全清{全清}/{所有关卡}")
requests.request("post","https://api-lbsns.feiyu.com/v1/user/gameDefaultRoleEdit",headers=headers2,json=data3)
re = requests.request("post","https://api-lbsns.feiyu.com/v1/user/gameDefaultRoleList",headers=headers,json=data)
rabbit=re.text
rabbit=json.loads(rabbit)
id=rabbit["data"]["list"][0]["game_role_id"]
name=rabbit["data"]["list"][0]["game_role_name"]
channel=rabbit["data"]["list"][0]["game_channel_name"]
关卡挑战=rabbit["data"]["list"][0]["stage_pass"]
所有关卡=rabbit["data"]["list"][0]["stage_count"]
金萝卜=rabbit["data"]["list"][0]["gold_carrot"]
全清=rabbit["data"]["list"][0]["clear"]
people2=(f"ID：{id}，用户名：{name}，渠道：{channel}，关卡挑战：{关卡挑战}/{所有关卡}，金萝卜：{金萝卜}/{所有关卡}，全清{全清}/{所有关卡}")
nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
all=f"{str(nowtime)}\n{people1}\n{people2}ok"
appToken = "AT_AGx1teOAFaGOuXUSl152QARxY6esRJ3Z"
uidres=requests.get("https://wxpusher.zjiecode.com/api/fun/wxuser/v2?appToken="+appToken)
uids=str(uidres.text)
data = json.loads(uids)
records = data["data"]["records"]
for i in records:
    uid=i["uid"]
    print(uid)
    body = {  
        "appToken": appToken,  
        "content": all,  
        "summary": "保卫萝卜提醒",  
        "contentType": 2,  
        "uids": [uid]
    }  
    response = requests.post("https://wxpusher.zjiecode.com/api/send/message/", json=body)  
    print(response.text)
