from datetime import datetime, timedelta  
from chinese_calendar import is_workday, is_holiday  
import requests  
  
# 获取当前时间  
now = datetime.now()  
print(f"当前时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")  
  
# 目标日期  
target_date = datetime(2024, 6, 23)  
  
# 初始化工作日计数  
work_days = 0  
current_date = now.date()  
  
# 循环遍历每一天，计算工作日  
while current_date <= target_date.date():  
    if is_workday(current_date) and not is_holiday(current_date):  
        work_days += 1  
    current_date += timedelta(days=1)  
  
# 格式化输出工作日数  
formatted_time = work_days
message=f"距离暑假剩余工作日天数:{formatted_time}天"


# 构建请求体并发送请求  
# 确保替换YOUR_APP_TOKEN和YOUR_UID为你从wxpusher获取的实际值  
appToken = "AT_mmtwbWXOSX9TnA1FfdhEtCHK5gwHmYg6"  
uids = ["UID_XZcjtnAUQrxbKFXq9YhRFMOipRYW"]  # 可以是多个UID组成的列表  
  
body = {  
    "appToken": appToken,  
    "content": "日常提醒",  
    "summary": message,  
    "contentType": 2,  
    "uids": uids  
}  
  
# 发送POST请求到wxpusher  
response = requests.post("https://wxpusher.zjiecode.com/api/send/message/", json=body)  
print(response.text)
