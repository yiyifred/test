import requests
import datetime

# 获取当前时间并输出
now = datetime.datetime.now()
print(f"当前时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")


# 计算距离2024年6月30日的日期，精确到秒
target_date = datetime.datetime(2024, 6, 30)
delta = target_date - now
print(f"距离暑假：{delta.days}天{delta.seconds // 3600}小时{(delta.seconds % 3600) // 60}分钟{delta.seconds % 60}秒")

a=f"距离暑假：{delta.days}天{delta.seconds // 3600}小时{(delta.seconds % 3600) // 60}分钟{delta.seconds % 60}秒"

body=\
    {
  "appToken":"AT_mmtwbWXOSX9TnA1FfdhEtCHK5gwHmYg6",
  "content":"日常提醒",
  "summary":a,
  "contentType":2,
  "uids":[
      "UID_XZcjtnAUQrxbKFXq9YhRFMOipRYW"
  ],
    }
r=requests.post("https://wxpusher.zjiecode.com/api/send/message/",json=body)
print(r.text)
