import requests

body=\
    {
  "appToken":"AT_mmtwbWXOSX9TnA1FfdhEtCHK5gwHmYg6",
  "content":"你好!",
  "summary":"这是一条测试消息",
  "contentType":1,
  "uids":[
      "UID_XZcjtnAUQrxbKFXq9YhRFMOipRYW"
  ],
    }
r=requests.post("https://wxpusher.zjiecode.com/api/send/message/",json=body)
print(r.text)