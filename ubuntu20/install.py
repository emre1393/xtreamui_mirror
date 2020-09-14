#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, os, random, string, sys, shutil, socket, zipfile, urllib2
from itertools import cycle, izip
from zipfile import ZipFile
from urllib2 import Request, urlopen, URLError, HTTPError

rDownloadURL = {"main": "https://bitbucket.org/emre1393/xtreamui_mirror/downloads/main_xtreamcodes_reborn.tar.gz", "sub": "https://bitbucket.org/emre1393/xtreamui_mirror/downloads/sub_xtreamcodes_reborn.tar.gz"}
rPackages = ["libcurl4", "curl", "php-pear", "libxslt1-dev", "libgeoip-dev", "e2fsprogs", "wget", "mcrypt", "nscd", "htop", "zip", "unzip", "mc", "mysql-server"]
rInstall = {"MAIN": "main", "LB": "sub"}
rUpdate = {"UPDATE": "update"}
rPhpUpdate = "https://github.com/emre1393/xtreamui_mirror/raw/master/ubuntu20/php_7.2.33_for_xc.zip"
rMySQLCnf = "IyBYdHJlYW0gQ29kZXMKCltjbGllbnRdCnBvcnQgICAgICAgICAgICA9IDMzMDYKCltteXNxbGRfc2FmZV0KbmljZSAgICAgICAgICAgID0gMAoKW215c3FsZF0KZGVmYXVsdC1hdXRoZW50aWNhdGlvbi1wbHVnaW49bXlzcWxfbmF0aXZlX3Bhc3N3b3JkCnVzZXIgICAgICAgICAgICA9IG15c3FsCnBvcnQgICAgICAgICAgICA9IDc5OTkKYmFzZWRpciAgICAgICAgID0gL3VzcgpkYXRhZGlyICAgICAgICAgPSAvdmFyL2xpYi9teXNxbAp0bXBkaXIgICAgICAgICAgPSAvdG1wCmxjLW1lc3NhZ2VzLWRpciA9IC91c3Ivc2hhcmUvbXlzcWwKc2tpcC1leHRlcm5hbC1sb2NraW5nCnNraXAtbmFtZS1yZXNvbHZlPTEKCmJpbmQtYWRkcmVzcyAgICAgICAgICAgID0gKgprZXlfYnVmZmVyX3NpemUgPSAxMjhNCgpteWlzYW1fc29ydF9idWZmZXJfc2l6ZSA9IDRNCm1heF9hbGxvd2VkX3BhY2tldCAgICAgID0gNjRNCm15aXNhbS1yZWNvdmVyLW9wdGlvbnMgPSBCQUNLVVAKbWF4X2xlbmd0aF9mb3Jfc29ydF9kYXRhID0gODE5MgoKYmlubG9nX2V4cGlyZV9sb2dzX3NlY29uZHMgPSA4NjQwMDAKbWF4X2JpbmxvZ19zaXplICAgICAgICAgPSAxMDBNCgptYXhfZXhlY3V0aW9uX3RpbWUgPSAwCnRyYW5zYWN0aW9uX2lzb2xhdGlvbiA9IFJFQUQtQ09NTUlUVEVECgptYXhfY29ubmVjdGlvbnMgID0gMTAwMDAKYmFja19sb2cgPSA0MDk2Cm9wZW5fZmlsZXNfbGltaXQgPSAxMDAwMAppbm5vZGJfb3Blbl9maWxlcyA9ODAwMAptYXhfY29ubmVjdF9lcnJvcnMgPSAzMDcyCnRhYmxlX29wZW5fY2FjaGUgPSA0MDk2CnRhYmxlX2RlZmluaXRpb25fY2FjaGUgPSA0MDk2CgoKdG1wX3RhYmxlX3NpemUgPSAxRwptYXhfaGVhcF90YWJsZV9zaXplID0gMUcKCmlubm9kYl9idWZmZXJfcG9vbF9zaXplID0gOEcKaW5ub2RiX2J1ZmZlcl9wb29sX2luc3RhbmNlcyA9IDE2Cmlubm9kYl9yZWFkX2lvX3RocmVhZHMgPSA2NAppbm5vZGJfd3JpdGVfaW9fdGhyZWFkcyA9IDY0Cmlubm9kYl90aHJlYWRfY29uY3VycmVuY3kgPSAwCmlubm9kYl9mbHVzaF9sb2dfYXRfdHJ4X2NvbW1pdCA9IDAKaW5ub2RiX2ZsdXNoX21ldGhvZCA9IE9fRElSRUNUCnBlcmZvcm1hbmNlX3NjaGVtYSA9IDAKaW5ub2RiLWZpbGUtcGVyLXRhYmxlID0gMQppbm5vZGJfaW9fY2FwYWNpdHk9MjAwMDAKaW5ub2RiX3RhYmxlX2xvY2tzID0gMAppbm5vZGJfbG9ja193YWl0X3RpbWVvdXQgPSAxMDAKaW5ub2RiX2RlYWRsb2NrX2RldGVjdCA9IDAKCgpzcWwtbW9kZT0iTk9fRU5HSU5FX1NVQlNUSVRVVElPTiIKCltteXNxbGR1bXBdCnF1aWNrCnF1b3RlLW5hbWVzCm1heF9hbGxvd2VkX3BhY2tldCAgICAgID0gMjRNCmNvbXBsZXRlLWluc2VydAoKW215c3FsXQoKW2lzYW1jaGtdCmtleV9idWZmZXJfc2l6ZSAgICAgICAgICAgICAgPSAxNk0=".decode("base64")

class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    YELLOW = '\033[33m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def generate(length=19): return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def getVersion():
    try: return subprocess.check_output("lsb_release -d".split()).split(":")[-1].strip()
    except: return ""

def printc(rText, rColour=col.OKBLUE, rPadding=0):
    print "%s ┌──────────────────────────────────────────┐ %s" % (rColour, col.ENDC)
    for i in range(rPadding): print "%s │                                          │ %s" % (rColour, col.ENDC)
    print "%s │ %s%s%s │ %s" % (rColour, " "*(20-(len(rText)/2)), rText, " "*(40-(20-(len(rText)/2))-len(rText)), col.ENDC)
    for i in range(rPadding): print "%s │                                          │ %s" % (rColour, col.ENDC)
    print "%s └──────────────────────────────────────────┘ %s" % (rColour, col.ENDC)
    print " "

def prepare(rType="MAIN"):
    global rPackages
    if rType <> "MAIN": rPackages = rPackages[:-1]
    printc("Preparing Installation")
    for rFile in ["/var/lib/dpkg/lock-frontend", "/var/cache/apt/archives/lock", "/var/lib/dpkg/lock"]:
        try: os.remove(rFile)
        except: pass
    os.system("apt-get update > /dev/null")
    for rPackage in rPackages:
        printc("Installing %s" % rPackage)
        os.system("apt-get install %s -y > /dev/null" % rPackage)
    printc("Installing libpng")
    os.system("wget -q -O /tmp/libpng12.deb http://ppa.launchpad.net/linuxuprising/libpng12/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1.1+1~ppa0~focal_amd64.deb") #https://launchpad.net/~linuxuprising/+archive/ubuntu/libpng12
    os.system("dpkg -i /tmp/libpng12.deb > /dev/null")
    os.system("apt-get install -y > /dev/null") # Clean up above
    try: os.remove("/tmp/libpng12.deb")
    except: pass
    try:
        subprocess.check_output("getent passwd xtreamcodes > /dev/null".split())
    except:
        # Create User
        printc("Creating user xtreamcodes")
        os.system("adduser --system --shell /bin/false --group --disabled-login xtreamcodes > /dev/null")
    if not os.path.exists("/home/xtreamcodes"): os.mkdir("/home/xtreamcodes")
    return True

def install(rType="MAIN"):
    global rInstall, rDownloadURL
    printc("Downloading Software")
    try: rURL = rDownloadURL[rInstall[rType]]
    except:
        printc("Invalid download URL!", col.FAIL)
        return False
    os.system('wget -q -O "/tmp/xtreamcodes.tar.gz" "%s"' % rURL)
    if os.path.exists("/tmp/xtreamcodes.tar.gz"):
        printc("Installing Software")
        os.system('tar -zxvf "/tmp/xtreamcodes.tar.gz" -C "/home/xtreamcodes/" > /dev/null')
        printc("Downloading PHP 7.4 Update")
        rPhplink = "%s" % rPhpUpdate
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib2.Request(rPhplink, headers=hdr)
        try:
    	    urllib2.urlopen(req)
        except:
            printc("Invalid download URL!", col.FAIL)
            return False
        print "\n"
        rURL = rPhplink
        os.system('wget -q -O "/tmp/phpupdate.zip" "%s"' % rURL)
        if os.path.exists("/tmp/phpupdate.zip"):
            try: is_ok = zipfile.ZipFile("/tmp/phpupdate.zip")
            except:
                printc("Invalid link or zip file is corrupted!", col.FAIL)
                os.remove("/tmp/phpupdate.zip")
                return False
            printc("Installing PHP 7.4 Update")
            os.system("unzip -qq -o /tmp/phpupdate.zip -d /")
        try: os.remove("/tmp/phpupdate.zip")
        except: pass
        try: os.remove("/tmp/xtreamcodes.tar.gz")
        except: pass
        return True
    printc("Failed to download installation file!", col.FAIL)
    return False

def update(rType="UPDATE"):
    printc("Enter the link of release_xyz.zip file:", col.WARNING)
    rlink = raw_input('Example: https://xtream-ui.com/releases/release_22f.zip\n\nNow enter the link:\n\n')
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = urllib2.Request(rlink, headers=hdr)
    try:
    	urllib2.urlopen(req)
    except:
        printc("Invalid download URL!", col.FAIL)
        return False
    print "\n"
    rURL = rlink
    printc("Installing python-paramiko")
    os.system("add-apt-repository universe > /dev/null && curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py --silent > /dev/null && python2 get-pip.py > /dev/null && yes | pip2 install paramiko > /dev/null")
    printc("Downloading Software Update")  
    print "\n"
    os.system('wget -q -O "/tmp/update.zip" "%s"' % rURL)
    if os.path.exists("/tmp/update.zip"):
        try: is_ok = zipfile.ZipFile("/tmp/update.zip")
        except:
            printc("Invalid link or zip file is corrupted!", col.FAIL)
            os.remove("/tmp/update.zip")
            return False
        printc("Updating Software")
        os.system('chattr -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null && rm -rf /home/xtreamcodes/iptv_xtream_codes/admin > /dev/null && rm -rf /home/xtreamcodes/iptv_xtream_codes/pytools > /dev/null && unzip -o /tmp/update.zip -d /tmp/update/ > /dev/null && cp -rf /tmp/update/XtreamUI-master/* /home/xtreamcodes/iptv_xtream_codes/ > /dev/null && rm -rf /tmp/update/XtreamUI-master > /dev/null && rm -rf /tmp/update > /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/ > /dev/null && chmod +x /home/xtreamcodes/iptv_xtream_codes/permissions.sh > /dev/null && chattr +i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null')
        if not "sudo chmod 400 /home/xtreamcodes/iptv_xtream_codes/config" in open("/home/xtreamcodes/iptv_xtream_codes/permissions.sh").read(): os.system('echo "#!/bin/bash\nsudo chmod -R 777 /home/xtreamcodes 2>/dev/null\nsudo find /home/xtreamcodes/iptv_xtream_codes/admin/ -type f -exec chmod 644 {} \; 2>/dev/null\nsudo find /home/xtreamcodes/iptv_xtream_codes/admin/ -type d -exec chmod 755 {} \; 2>/dev/null\nsudo find /home/xtreamcodes/iptv_xtream_codes/wwwdir/ -type f -exec chmod 644 {} \; 2>/dev/null\nsudo find /home/xtreamcodes/iptv_xtream_codes/wwwdir/ -type d -exec chmod 755 {} \; 2>/dev/null\nsudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx 2>/dev/null\nsudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/sbin/nginx_rtmp 2>/dev/null\nchmod -R 0644 /home/xtreamcodes/iptv_xtream_codes/php/*.pid\nsudo chmod 400 /home/xtreamcodes/iptv_xtream_codes/config 2>/dev/null" > /home/xtreamcodes/iptv_xtream_codes/permissions.sh')
        os.system("sed -i 's|/usr/bin/python|/usr/bin/python2|g' /home/xtreamcodes/iptv_xtream_codes/admin/functions.php && sed -i 's|/usr/bin/python|/usr/bin/python2|g' /home/xtreamcodes/iptv_xtream_codes/crons/balancer.php && sed -i 's|python|python2|g' /home/xtreamcodes/iptv_xtream_codes/pytools/balancer.py && sed -i 's|/usr/bin/env python|/usr/bin/env python2.7|g' /home/xtreamcodes/iptv_xtream_codes/pytools/PTN/*.py")  #for python2
        os.system("/home/xtreamcodes/iptv_xtream_codes/permissions.sh > /dev/null")
        try: os.remove("/tmp/update.zip")
        except: pass
        return True
    printc("Failed to download installation file!", col.FAIL)
    return False


def mysql(rUsername, rPassword):
    global rMySQLCnf
    printc("Configuring MySQL")
    rCreate = True
    if os.path.exists("/etc/mysql/my.cnf"):
        if open("/etc/mysql/my.cnf", "r").read(14) == "# Xtream Codes": rCreate = False
    if rCreate:
        shutil.copy("/etc/mysql/my.cnf", "/etc/mysql/my.cnf.xc")
        rFile = open("/etc/mysql/my.cnf", "w")
        rFile.write(rMySQLCnf)
        rFile.close()
        os.system("service mysql restart > /dev/null")
    printc("Enter MySQL Root Password:", col.WARNING)
    for i in range(5):
        rMySQLRoot = raw_input("  ")
        print " "
        if len(rMySQLRoot) > 0: rExtra = " -p%s" % rMySQLRoot
        else: rExtra = ""
        printc("Drop existing & create database? Y/N", col.WARNING)
        if raw_input("  ").upper() == "Y": rDrop = True
        else: rDrop = False
        try:
            if rDrop:
                os.system('mysql -u root%s -e "DROP DATABASE IF EXISTS xtream_iptvpro; CREATE DATABASE IF NOT EXISTS xtream_iptvpro;" > /dev/null' % rExtra)
                os.system("mysql -u root%s xtream_iptvpro < /home/xtreamcodes/iptv_xtream_codes/database.sql > /dev/null" % rExtra)
                os.system('mysql -u root%s -e "USE xtream_iptvpro; UPDATE settings SET live_streaming_pass = \'%s\', unique_id = \'%s\', crypt_load_balancing = \'%s\', get_real_ip_client=\'\';" > /dev/null' % (rExtra, generate(20), generate(10), generate(20)))
                os.system('mysql -u root%s -e "USE xtream_iptvpro; REPLACE INTO streaming_servers (id, server_name, domain_name, server_ip, vpn_ip, ssh_password, ssh_port, diff_time_main, http_broadcast_port, total_clients, system_os, network_interface, latency, status, enable_geoip, geoip_countries, last_check_ago, can_delete, server_hardware, total_services, persistent_connections, rtmp_port, geoip_type, isp_names, isp_type, enable_isp, boost_fpm, http_ports_add, network_guaranteed_speed, https_broadcast_port, https_ports_add, whitelist_ips, watchdog_data, timeshift_only) VALUES (1, \'Main Server\', \'\', \'%s\', \'\', NULL, NULL, 0, 25461, 1000, \'%s\', \'eth0\', 0, 1, 0, \'\', 0, 0, \'{}\', 3, 0, 25462, \'low_priority\', \'\', \'low_priority\', 0, 1, \'\', 1000, 25463, \'\', \'[\"127.0.0.1\",\"\"]\', \'{}\', 0);" > /dev/null' % (rExtra, getIP(), getVersion()))
                os.system('mysql -u root%s -e "USE xtream_iptvpro; REPLACE INTO reg_users (id, username, password, email, member_group_id, verified, status) VALUES (1, \'admin\', \'\$6\$rounds=20000\$xtreamcodes\$XThC5OwfuS0YwS4ahiifzF14vkGbGsFF1w7ETL4sRRC5sOrAWCjWvQJDromZUQoQuwbAXAFdX3h3Cp3vqulpS0\', \'admin@website.com\', 1, 1, 1);" > /dev/null'  % rExtra)
                os.system('mysql -u root%s -e "CREATE USER \'%s\'@\'%%\' IDENTIFIED WITH mysql_native_password BY \'%s\'; GRANT ALL PRIVILEGES ON xtream_iptvpro.* TO \'%s\'@\'%%\' WITH GRANT OPTION; GRANT SELECT, LOCK TABLES ON *.* TO \'%s\'@\'%%\'; FLUSH PRIVILEGES;" > /dev/null' % (rExtra, rUsername, rPassword, rUsername, rUsername))
                os.system('mysql -u root%s -e "USE xtream_iptvpro; CREATE TABLE IF NOT EXISTS dashboard_statistics (id int(11) NOT NULL AUTO_INCREMENT, type varchar(16) NOT NULL DEFAULT \'\', time int(16) NOT NULL DEFAULT \'0\', count int(16) NOT NULL DEFAULT \'0\', PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=latin1; INSERT INTO dashboard_statistics (type, time, count) VALUES(\'conns\', UNIX_TIMESTAMP(), 0),(\'users\', UNIX_TIMESTAMP(), 0);\" > /dev/null' % rExtra)
            try: os.remove("/home/xtreamcodes/iptv_xtream_codes/database.sql")
            except: pass
            return True
        except: printc("Invalid password! Try again", col.FAIL)
    return False

def encrypt(rHost="127.0.0.1", rUsername="user_iptvpro", rPassword="", rDatabase="xtream_iptvpro", rServerID=1, rPort=7999):
    printc("Encrypting...")
    try: os.remove("/home/xtreamcodes/iptv_xtream_codes/config")
    except: pass
    rf = open('/home/xtreamcodes/iptv_xtream_codes/config', 'wb')
    rf.write(''.join(chr(ord(c)^ord(k)) for c,k in izip('{\"host\":\"%s\",\"db_user\":\"%s\",\"db_pass\":\"%s\",\"db_name\":\"%s\",\"server_id\":\"%d\", \"db_port\":\"%d\"}' % (rHost, rUsername, rPassword, rDatabase, rServerID, rPort), cycle('5709650b0d7806074842c6de575025b1'))).encode('base64').replace('\n', ''))
    rf.close()

def configure():
    printc("Configuring System")
    if not "/home/xtreamcodes/iptv_xtream_codes/" in open("/etc/fstab").read():
        rFile = open("/etc/fstab", "a")
        rFile.write("tmpfs /home/xtreamcodes/iptv_xtream_codes/streams tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777,size=90% 0 0\ntmpfs /home/xtreamcodes/iptv_xtream_codes/tmp tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777,size=2G 0 0")
        rFile.close()
    if not "xtreamcodes" in open("/etc/sudoers").read():
        os.system('echo "xtreamcodes ALL = (root) NOPASSWD: /sbin/iptables, /usr/bin/chattr" >> /etc/sudoers')
    if not os.path.exists("/etc/init.d/xtreamcodes"):
        rFile = open("/etc/init.d/xtreamcodes", "w")
        rFile.write("#! /bin/bash\n/home/xtreamcodes/iptv_xtream_codes/start_services.sh")
        rFile.close()
        os.system("chmod +x /etc/init.d/xtreamcodes > /dev/null")
    try: os.remove("/usr/bin/ffmpeg")
    except: pass
    if not os.path.exists("/home/xtreamcodes/iptv_xtream_codes/tv_archive"): os.mkdir("/home/xtreamcodes/iptv_xtream_codes/tv_archive/")
    os.system("ln -s /home/xtreamcodes/iptv_xtream_codes/bin/ffmpeg /usr/bin/")
    os.system("chattr -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null")
    os.system("wget -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/GeoLite2.mmdb -O /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb")
    os.system("wget -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/pid_monitor.php -O /home/xtreamcodes/iptv_xtream_codes/crons/pid_monitor.php")
    os.system("chown xtreamcodes:xtreamcodes -R /home/xtreamcodes > /dev/null")
    os.system("chmod -R 0777 /home/xtreamcodes > /dev/null")
    os.system("chmod -R 0644 /home/xtreamcodes/iptv_xtream_codes/php/*.pid > /dev/null")
    os.system("chattr +i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null")
    os.system("sed -i 's|chown -R xtreamcodes:xtreamcodes /home/xtreamcodes|chown -R xtreamcodes:xtreamcodes /home/xtreamcodes 2>/dev/null|g' /home/xtreamcodes/iptv_xtream_codes/start_services.sh")
    os.system("chmod +x /home/xtreamcodes/iptv_xtream_codes/start_services.sh > /dev/null")
    os.system("mount -a")
    os.system("chmod 0700 /home/xtreamcodes/iptv_xtream_codes/config > /dev/null")
    os.system("sed -i 's|echo \"Xtream Codes Reborn\";|header(\"Location: https://www.google.com/\");|g' /home/xtreamcodes/iptv_xtream_codes/wwwdir/index.php")
    if not "api.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    api.xtream-codes.com" >> /etc/hosts')
    if not "downloads.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    downloads.xtream-codes.com" >> /etc/hosts')
    if not "xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    xtream-codes.com" >> /etc/hosts')
    if not "@reboot root /home/xtreamcodes/iptv_xtream_codes/start_services.sh" in open("/etc/crontab").read(): os.system('echo "@reboot root /home/xtreamcodes/iptv_xtream_codes/start_services.sh" >> /etc/crontab')

def start(first=True):
    if first: printc("Starting Xtream Codes")
    else: printc("Restarting Xtream Codes")
    os.system("/home/xtreamcodes/iptv_xtream_codes/start_services.sh > /dev/null")

def modifyNginx():
    printc("Modifying Nginx")
    rPath = "/home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf"
    rPrevData = open(rPath, "r").read()
    if not "listen 25500;" in rPrevData:
        shutil.copy(rPath, "%s.xc" % rPath)
        rData = "}".join(rPrevData.split("}")[:-1]) + "    server {\n        listen 25500;\n        index index.php index.html index.htm;\n        root /home/xtreamcodes/iptv_xtream_codes/admin/;\n\n        location ~ \.php$ {\n			limit_req zone=one burst=8;\n            try_files $uri =404;\n			fastcgi_index index.php;\n			fastcgi_pass php;\n			include fastcgi_params;\n			fastcgi_buffering on;\n			fastcgi_buffers 96 32k;\n			fastcgi_buffer_size 32k;\n			fastcgi_max_temp_file_size 0;\n			fastcgi_keep_conn on;\n			fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;\n			fastcgi_param SCRIPT_NAME $fastcgi_script_name;\n        }\n    }\n}"
        rFile = open(rPath, "w")
        rFile.write(rData)
        rFile.close()

if __name__ == "__main__":
    printc("Xtream Codes Reborn BETA - Installer", col.OKGREEN, 2)
    print "%s │ NOTE: this is a forked mirror of original installer from https://xtream-ui.com/install/install.py %s" % (col.OKGREEN, col.ENDC)
    print "%s │ Check out the mirror repo: https://bitbucket.org/emre1393/xtreamui_mirror/ and https://github.com/emre1393/xtreamui_mirror %s" % (col.OKGREEN, col.ENDC)
    print " "
    rType = raw_input("  Installation Type [MAIN, LB, UPDATE]: ")
    print " "
    if rType.upper() in ["MAIN", "LB"]:
        if rType.upper() == "LB":
            rHost = raw_input("  Main Server IP Address: ")
            rPassword = raw_input("  MySQL Password: ")
            try: rServerID = int(raw_input("  Load Balancer Server ID: "))
            except: rServerID = -1
            print " "
        else:
            rHost = "127.0.0.1"
            rPassword = generate()
            rServerID = 1
        rUsername = "user_iptvpro"
        rDatabase = "xtream_iptvpro"
        rPort = 7999
        if len(rHost) > 0 and len(rPassword) > 0 and rServerID > -1:
            printc("Start installation? Y/N", col.WARNING)
            if raw_input("  ").upper() == "Y":
                print " "
                rRet = prepare(rType.upper())
                if not install(rType.upper()): sys.exit(1)
                if rType.upper() == "MAIN":
                    if not mysql(rUsername, rPassword): sys.exit(1)
                encrypt(rHost, rUsername, rPassword, rDatabase, rServerID, rPort)
                configure()
                if rType.upper() == "MAIN": modifyNginx()
                start()
                printc("Installation completed!", col.OKGREEN, 2)
                if rType.upper() == "MAIN":
                    printc("Please store your MySQL password!")
                    printc(rPassword)
                    printc("Admin UI: http://%s:25500" % getIP())
                    printc("Install Admin UI with UPDATE option.")
                    printc("Admin UI default login is admin/admin")
            else: printc("Installation cancelled", col.FAIL)
        else: printc("Invalid entries", col.FAIL)
    elif rType.upper() == "UPDATE":
        if os.path.exists("/home/xtreamcodes/iptv_xtream_codes/wwwdir/api.php"):
            printc("Install/Update Admin Panel? Y/N?", col.WARNING)
            if raw_input("  ").upper() == "Y":
                if not update(rType.upper()): sys.exit(1)
                printc("Installation completed!", col.OKGREEN, 2)
                start()
        else: printc("Install Xtream Codes Main first!", col.FAIL)
    else: printc("Invalid installation type", col.FAIL)
