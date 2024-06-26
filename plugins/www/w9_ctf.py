#!/usr/bin/env python
import urllib.parse


def assign(service, arg):
    if service != "www":
        return
    arr = urllib.parse.urlparse(arg)
    return True, '%s://%s/' % (arr.scheme, arr.netloc)
    # return True, arg


def audit(arg):
    urls = '''
.git
.git/HEAD
.git/index
.git/config
.git/description
README.MD
README.md
README
.gitignore
.svn
.svn/wc.db
.svn/entries
user.php.bak
.hg
.DS_store
WEB-INF/web.xml
WEB-INF/src/
WEB-INF/classes
WEB-INF/lib
WEB-INF/database.propertie
CVS/Root
CVS/Entries
.bzr/
%3f
%3f~
.%3f.swp
.%3f.swo
.%3f.swn
.%3f.swm
.%3f.swl
_viminfo
.viminfo
%3f~
%3f~1~
%3f~2~
%3f~3~
%3f.save
%3f.save1
%3f.save2
%3f.save3
%3f.bak_Edietplus
%3f.bak
%3f.back
phpinfo.php
robots.txt
.htaccess
.bash_history
.svn/
.git/
.index.php.swp
index.php.swp
index.php.bak
.index.php~
index.php.bak_Edietplus
index.php.~
index.php.~1~
index.php
index.php~
index.php.rar
index.php.zip
index.php.7z
index.php.tar.gz
index.php.txt
login.php
register.php
test.php
upload.php
phpinfo.php
t.php
www.zip
www.rar
www.zip
www.7z
www.tar.gz
www.tar
web.zip
web.rar
web.zip
web.7z
web.tar.gz
web.tar
plus
qq.txt
log.txt
wwwroot.rar
web.rar
dede
admin
edit
Fckeditor
ewebeditor
bbs
Editor
manage
shopadmin
web_Fckeditor
login
webadmin
admin/WebEditor
admin/daili/webedit
login/
database/
tmp/
manager/
manage/
web/
admin/
shopadmin/
wp-includes/
edit/
editor/
user/
users/
admin/
home/
test/
administrator/
houtai/
backdoor/
flag/
upload/
uploads/
download/
downloads/
manager/
root.zip
root.rar
wwwroot.zip
wwwroot.rar
backup.zip
backup.rar
.svn/entries
.git/config
.ds_store
flag.php
fl4g.php
f1ag.php
f14g.php
admin.php
4dmin.php
adm1n.php
4dm1n.php
admin1.php
admin2.php
adminlogin.php
administrator.php
login.php
register.php
upload.php
home.php
log.php
logs.php
config.php
member.php
user.php
users.php
robots.php
info.php
phpinfo.php
backdoor.php
fm.php
example.php
mysql.bak
a.sql
b.sql
db.sql
bdb.sql
ddb.sql
users.sql
mysql.sql
dump.sql
data.sql
backup.sql
backup.sql.gz
backup.sql.bz2
backup.zip
rss.xml
crossdomain.xml
1.txt
flag.txt
configuration.php
sites/default/settings.php
config.php
config.inc.php
conf/_basic_config.php
config/site.php
system/config/default.php
framework/conf/config.php
mysite/_config.php
typo3conf/localconf.php
config/config_global.php
config/config_ucenter.php
lib
data/config.php
data/config.inc.php
includes/config.php
data/common.inc.php
caches/configs/database.php
caches/configs/system.php
include/config.inc.php
phpsso_server/caches/configs/database.php
phpsso_server/caches/configs/system.php
404.php
index.html
user/
users/
admin/
home/
test/
administrator/
houtai/
backdoor/
flag/
uploads/
download/
downloads/
manager/
phpmyadmin/
phpMyAdmin/
log/access.log
    '''

    for x in urls.strip().splitlines():
        try:
            code, head, body, redirect, log = hackhttp.http(arg + x)
            if code != 404:
                msg = {
                    "url": arg + x,
                    "length": len(body),
                    "status_code": code
                }
                security_info(repr(msg), "ctfscan")
        except:
            pass


if __name__ == '__main__':
    from dummy import *

    audit(assign('www', 'http://blog.hacking8.com/')[1])
