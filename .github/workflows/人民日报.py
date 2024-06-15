import datetime
import os
import time
import requests
from PyPDF2 import PdfMerger
import requests
import shutil
 
pdf_folder = r'人民日报下载目录'
today = datetime.date.today()
formatted_date = today.strftime("%Y-%m/%d")
filename_num = formatted_date.replace("-", "").replace("/", "")
pdf_cache = pdf_folder + f"/cache/{filename_num}"
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)
if not os.path.exists(pdf_cache):
    os.makedirs(pdf_cache)
# 下载单个PDF文件的函数
def download_pdf(url):
    try:
        # 发送GET请求获取文件内容
        response = requests.get(url)
        # 检查响应状态码
        if response.status_code != 200:
            print(f"文件 {url} 不存在，跳过。")
            return None
        # 生成本地文件名
        filename = os.path.join(pdf_cache, url.split('/')[-1])
        # 将文件内容保存到本地磁盘
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"已下载文件 {filename}")
        return filename
    except Exception as e:
        line_err = f'error line:{e.__traceback__.tb_lineno}'
        print(f"异常行-{line_err}  异常信息：{str(e)}")
 
# 组合今天的各版下载链接列表
def url_list():
    try:
        pdf_urls = []
        for i in range(1, 21):
            if i < 10:
                ban_i = ("0" + str(i))[-2:]
            else:
                ban_i =  str(i)
            pdf_urls.append(f"http://paper.people.com.cn/rmrb/images/{formatted_date}/{ban_i}/rmrb{filename_num}{ban_i}.pdf")
    except Exception as e:
        line_err = f'error line:{e.__traceback__.tb_lineno}'
        print(f"异常行-{line_err}  异常信息：{str(e)}")
        pdf_urls = []
    return pdf_urls
# 合并各版pdf
def pdf_merge():
    try:
        # 创建一个PdfFileMerger对象
        merger = PdfMerger()
        for filename in os.listdir(pdf_cache):
            if filename.endswith(".pdf"):
                file_path = os.path.join(pdf_cache, filename)
                merger.append(file_path)
        output_filename = os.path.join(pdf_folder, filename_num + ".pdf")
        with open(output_filename, "wb") as outfile:
            merger.write(outfile)
            merger.close()
    except Exception as e:
        line_err = f'error line:{e.__traceback__.tb_lineno}'
        print(f"异常行-{line_err}  异常信息：{str(e)}")
# 合并各版pdf
def main():
    try:
        start_time = time.time()
        pdf_urls = url_list()
        for url_i in pdf_urls:
            download_pdf(url_i)
        pdf_merge()
        # 结束计时
        end_time = time.time()
        # 计算并打印运行时间
        elapsed_time = end_time - start_time
        print(f"总共下载PDF文件，用时 {elapsed_time:.2f} 秒。")
        shutil.rmtree(pdf_cache)
        # body=\
        #     {
        # "appToken":"AT_mmtwbWXOSX9TnA1FfdhEtCHK5gwHmYg6",
        # "content":"人民日报提醒",
        # "summary":f"下载人民日报：用时 {elapsed_time:.2f} 秒。",
        # "contentType":1,
        # "uids":[
        #     "UID_XZcjtnAUQrxbKFXq9YhRFMOipRYW"
        # ],
        #     }
        # r=requests.post("https://wxpusher.zjiecode.com/api/send/message/",json=body)
        # print(r.text)
    except Exception as e:
        line_err = f'error line:{e.__traceback__.tb_lineno}'
        print(f"异常行-{line_err}  异常信息：{str(e)}")
 
if __name__ == '__main__':
    main()
