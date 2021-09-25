#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, os, random, string, sys, shutil, socket, zipfile, urllib2
from itertools import cycle, izip
from zipfile import ZipFile

rDownloadURL = {"main": "https://bitbucket.org/emre1393/xtreamui_mirror/downloads/main_xtreamcodes_reborn.tar.gz", "sub": "https://bitbucket.org/emre1393/xtreamui_mirror/downloads/sub_xtreamcodes_reborn.tar.gz"}
rPackages = ["libcurl3", "libxslt1-dev", "libgeoip-dev", "e2fsprogs", "wget", "mcrypt", "nscd", "htop", "zip", "unzip", "mc", "libjemalloc1", "python-paramiko", "mysql-server"]
rInstall = {"MAIN": "main", "LB": "sub"}
rMySQLCnf = "IyBYdHJlYW0gQ29kZXMKCltjbGllbnRdCnBvcnQgICAgICAgICAgICA9IDMzMDYKCltteXNxbGRfc2FmZV0KbmljZSAgICAgICAgICAgID0gMAoKW215c3FsZF0KZGVmYXVsdC1hdXRoZW50aWNhdGlvbi1wbHVnaW49bXlzcWxfbmF0aXZlX3Bhc3N3b3JkCnVzZXIgICAgICAgICAgICA9IG15c3FsCnBvcnQgICAgICAgICAgICA9IDc5OTkKYmFzZWRpciAgICAgICAgID0gL3VzcgpkYXRhZGlyICAgICAgICAgPSAvdmFyL2xpYi9teXNxbAp0bXBkaXIgICAgICAgICAgPSAvdG1wCgpsYy1tZXNzYWdlcy1kaXIgPSAvdXNyL3NoYXJlL215c3FsCnNraXAtZXh0ZXJuYWwtbG9ja2luZwpza2lwLW5hbWUtcmVzb2x2ZT0xCgpiaW5kLWFkZHJlc3MgICAgICAgICAgICA9ICoKCmtleV9idWZmZXJfc2l6ZSA9IDEyOE0KbXlpc2FtX3NvcnRfYnVmZmVyX3NpemUgPSA0TQptYXhfYWxsb3dlZF9wYWNrZXQgICAgICA9IDY0TQpteWlzYW0tcmVjb3Zlci1vcHRpb25zID0gQkFDS1VQCm1heF9sZW5ndGhfZm9yX3NvcnRfZGF0YSA9IDgxOTIKcXVlcnlfY2FjaGVfbGltaXQgPSAwCnF1ZXJ5X2NhY2hlX3NpemUgPSAwCnF1ZXJ5X2NhY2hlX3R5cGUgPSAwCgpleHBpcmVfbG9nc19kYXlzID0gMTAKI2JpbmxvZ19leHBpcmVfbG9nc19zZWNvbmRzID0gODY0MDAwCm1heF9iaW5sb2dfc2l6ZSA9IDEwME0KdHJhbnNhY3Rpb25faXNvbGF0aW9uID0gUkVBRC1DT01NSVRURUQKbWF4X2Nvbm5lY3Rpb25zICA9IDEwMDAwCm9wZW5fZmlsZXNfbGltaXQgPSAxMDI0MAppbm5vZGJfb3Blbl9maWxlcyA9MTAyNDAKbWF4X2Nvbm5lY3RfZXJyb3JzID0gNDA5Ngp0YWJsZV9vcGVuX2NhY2hlID0gNDA5Ngp0YWJsZV9kZWZpbml0aW9uX2NhY2hlID0gNDA5Ngp0bXBfdGFibGVfc2l6ZSA9IDFHCm1heF9oZWFwX3RhYmxlX3NpemUgPSAxRwptYXhfZXhlY3V0aW9uX3RpbWUgPSAwCmJhY2tfbG9nID0gNDA5NgoKaW5ub2RiX2J1ZmZlcl9wb29sX3NpemUgPSA4Rwppbm5vZGJfYnVmZmVyX3Bvb2xfaW5zdGFuY2VzID0gOAppbm5vZGJfcmVhZF9pb190aHJlYWRzID0gNjQKaW5ub2RiX3dyaXRlX2lvX3RocmVhZHMgPSA2NAppbm5vZGJfdGhyZWFkX2NvbmN1cnJlbmN5ID0gMAppbm5vZGJfZmx1c2hfbG9nX2F0X3RyeF9jb21taXQgPSAwCmlubm9kYl9mbHVzaF9tZXRob2QgPSBPX0RJUkVDVApwZXJmb3JtYW5jZV9zY2hlbWEgPSAwCmlubm9kYi1maWxlLXBlci10YWJsZSA9IDEKaW5ub2RiX2lvX2NhcGFjaXR5ID0gMTAwMDAKaW5ub2RiX3RhYmxlX2xvY2tzID0gMAppbm5vZGJfbG9ja193YWl0X3RpbWVvdXQgPSAwCmlubm9kYl9kZWFkbG9ja19kZXRlY3QgPSAwCmlubm9kYl9sb2dfZmlsZV9zaXplID0gMUcKCnNxbC1tb2RlPSJOT19FTkdJTkVfU1VCU1RJVFVUSU9OIgoKCltteXNxbGR1bXBdCnF1aWNrCnF1b3RlLW5hbWVzCm1heF9hbGxvd2VkX3BhY2tldCAgICAgID0gMTI4TQpjb21wbGV0ZS1pbnNlcnQKCltteXNxbF0KCltpc2FtY2hrXQprZXlfYnVmZmVyX3NpemUgICAgICAgICAgICAgID0gMTZN==".decode("base64")
rMySQLServiceFile = "IyBNeVNRTCBzeXN0ZW1kIHNlcnZpY2UgZmlsZQoKW1VuaXRdCkRlc2NyaXB0aW9uPU15U1FMIENvbW11bml0eSBTZXJ2ZXIKQWZ0ZXI9bmV0d29yay50YXJnZXQKCltJbnN0YWxsXQpXYW50ZWRCeT1tdWx0aS11c2VyLnRhcmdldAoKW1NlcnZpY2VdClR5cGU9Zm9ya2luZwpVc2VyPW15c3FsCkdyb3VwPW15c3FsClBJREZpbGU9L3J1bi9teXNxbGQvbXlzcWxkLnBpZApQZXJtaXNzaW9uc1N0YXJ0T25seT10cnVlCkV4ZWNTdGFydFByZT0vdXNyL3NoYXJlL215c3FsL215c3FsLXN5c3RlbWQtc3RhcnQgcHJlCkV4ZWNTdGFydD0vdXNyL3NiaW4vbXlzcWxkIC0tZGFlbW9uaXplIC0tcGlkLWZpbGU9L3J1bi9teXNxbGQvbXlzcWxkLnBpZCAtLW1heC1leGVjdXRpb24tdGltZT0wCkVudmlyb25tZW50RmlsZT0tL2V0Yy9teXNxbC9teXNxbGQKVGltZW91dFNlYz02MDAKUmVzdGFydD1vbi1mYWlsdXJlClJ1bnRpbWVEaXJlY3Rvcnk9bXlzcWxkClJ1bnRpbWVEaXJlY3RvcnlNb2RlPTc1NQpMaW1pdE5PRklMRT01MDAw==".decode("base64")
# i am lazy to prepare echo versions with escaped characters, use base64 decode/encode to read or change these.

rVersions = {
    "16.04": "xenial",
    "18.04": "bionic"
}

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

def generate(length=32): return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

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
    if rType <> "MAIN": rPackages = rPackages[:-3]
    printc("Preparing Installation")
    for rFile in ["/var/lib/dpkg/lock-frontend", "/var/cache/apt/archives/lock", "/var/lib/dpkg/lock"]:
        try: os.remove(rFile)
        except: pass
    os.system("apt-get update > /dev/null")
    printc("Removing libcurl4 if installed")
    os.system("apt-get remove --auto-remove libcurl4 -y > /dev/null")
    for rPackage in rPackages:
        printc("Installing %s" % rPackage)
        os.system("apt-get install %s -y > /dev/null" % rPackage)
    printc("Installing libpng")
    os.system("wget -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb")
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
        if os.path.exists("/home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb"):
            os.system('chattr -f -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null')
        os.system('tar -zxvf "/tmp/xtreamcodes.tar.gz" -C "/home/xtreamcodes/" > /dev/null')
        try: os.remove("/tmp/xtreamcodes.tar.gz")
        except: pass
        return True
    printc("Failed to download installation file!", col.FAIL)
    return False


def installadminpanel():
    rURL = "https://bitbucket.org/emre1393/xtreamui_mirror/downloads/release_22f.zip"
    printc("Downloading Admin Panel")  
    os.system('wget -q -O "/tmp/update.zip" "%s"' % rURL)
    if os.path.exists("/tmp/update.zip"):
        try: is_ok = zipfile.ZipFile("/tmp/update.zip")
        except:
            printc("Invalid link or zip file is corrupted!", col.FAIL)
            os.remove("/tmp/update.zip")
            return False
    printc("Installing Admin Panel")
    os.system('unzip -o /tmp/update.zip -d /tmp/update/ > /dev/null && cp -rf /tmp/update/XtreamUI-master/* /home/xtreamcodes/iptv_xtream_codes/ > /dev/null && rm -rf /tmp/update/XtreamUI-master > /dev/null && rm -rf /tmp/update > /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes > /dev/null')
    try: os.remove("/tmp/update.zip")
    except: pass
    rURL2 = "https://bitbucket.org/emre1393/xtreamui_mirror/downloads/newstuff.zip"
    printc("Downloading New Stuff for Admin Panel")  
    os.system('wget -q -O "/tmp/update2.zip" "%s"' % rURL2)
    if os.path.exists("/tmp/update2.zip"):
        try: is_ok = zipfile.ZipFile("/tmp/update2.zip")
        except:
            printc("Invalid link or zip file is corrupted!", col.FAIL)
            os.remove("/tmp/update2.zip")
            return False
        printc("Installing New Stuff for Admin Panel")
        os.system('unzip -o /tmp/update2.zip -d /tmp/update2/ > /dev/null && cp -rf /tmp/update2/* /home/xtreamcodes/iptv_xtream_codes/ > /dev/null && rm -rf /tmp/update2/* > /dev/null && rm -rf /tmp/update2 > /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/ > /dev/null > /dev/null')
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
                os.system('mysql -u root%s -e "DROP USER IF EXISTS \'%s\'@\'%%\'; DROP USER IF EXISTS \'%s\'@\'localhost\'; DROP USER IF EXISTS \'%s\'@\'127.0.0.1\';" > /dev/null' % (rExtra, rUsername, rUsername, rUsername))
                os.system('mysql -u root%s -e "DROP DATABASE IF EXISTS xtream_iptvpro; CREATE DATABASE IF NOT EXISTS xtream_iptvpro;" > /dev/null' % rExtra)
                os.system("mysql -u root%s xtream_iptvpro < /home/xtreamcodes/iptv_xtream_codes/database.sql > /dev/null" % rExtra)
                os.system('mysql -u root%s -e "USE xtream_iptvpro; UPDATE settings SET live_streaming_pass = \'%s\', unique_id = \'%s\', crypt_load_balancing = \'%s\', get_real_ip_client=\'\';" > /dev/null' % (rExtra, generate(20), generate(12), generate(20)))
                os.system('mysql -u root%s -e "USE xtream_iptvpro; REPLACE INTO streaming_servers (id, server_name, domain_name, server_ip, vpn_ip, ssh_password, ssh_port, diff_time_main, http_broadcast_port, total_clients, system_os, network_interface, latency, status, enable_geoip, geoip_countries, last_check_ago, can_delete, server_hardware, total_services, persistent_connections, rtmp_port, geoip_type, isp_names, isp_type, enable_isp, boost_fpm, http_ports_add, network_guaranteed_speed, https_broadcast_port, https_ports_add, whitelist_ips, watchdog_data, timeshift_only) VALUES (1, \'Main Server\', \'\', \'%s\', \'\', NULL, NULL, 0, 8080, 1000, \'%s\', \'eth0\', 0, 1, 0, \'\', 0, 0, \'{}\', 3, 0, 8880, \'low_priority\', \'\', \'low_priority\', 0, 1, \'\', 1000, 8443, \'\', \'[\"127.0.0.1\",\"\"]\', \'{}\', 0);" > /dev/null' % (rExtra, getIP(), getVersion()))
                os.system('mysql -u root%s -e "USE xtream_iptvpro; REPLACE INTO reg_users (id, username, password, email, member_group_id, verified, status) VALUES (1, \'admin\', \'\$6\$rounds=20000\$xtreamcodes\$XThC5OwfuS0YwS4ahiifzF14vkGbGsFF1w7ETL4sRRC5sOrAWCjWvQJDromZUQoQuwbAXAFdX3h3Cp3vqulpS0\', \'admin@website.com\', 1, 1, 1);" > /dev/null'  % rExtra)
                os.system('mysql -u root%s -e "CREATE USER \'%s\'@\'localhost\' IDENTIFIED BY \'%s\'; GRANT ALL PRIVILEGES ON xtream_iptvpro.* TO \'%s\'@\'localhost\' WITH GRANT OPTION; GRANT SELECT, PROCESS, LOCK TABLES ON *.* TO \'%s\'@\'%%\';FLUSH PRIVILEGES;" > /dev/null' % (rExtra, rUsername, rPassword, rUsername, rUsername))
                os.system('mysql -u root%s -e "CREATE USER \'%s\'@\'127.0.0.1\' IDENTIFIED BY \'%s\'; GRANT ALL PRIVILEGES ON xtream_iptvpro.* TO \'%s\'@\'127.0.0.1\' WITH GRANT OPTION; GRANT SELECT, PROCESS, LOCK TABLES ON *.* TO \'%s\'@\'%%\';FLUSH PRIVILEGES;" > /dev/null' % (rExtra, rUsername, rPassword, rUsername, rUsername))
                os.system('mysql -u root%s -e "GRANT SELECT, INSERT, UPDATE, DELETE ON xtream_iptvpro.* TO \'%s\'@\'%%\' IDENTIFIED BY \'%s\';FLUSH PRIVILEGES;" > /dev/null' % (rExtra, rUsername, rPassword))
                os.system('mysql -u root%s -e "USE xtream_iptvpro; CREATE TABLE IF NOT EXISTS dashboard_statistics (id int(11) NOT NULL AUTO_INCREMENT, type varchar(16) NOT NULL DEFAULT \'\', time int(16) NOT NULL DEFAULT \'0\', count int(16) NOT NULL DEFAULT \'0\', PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=latin1; INSERT INTO dashboard_statistics (type, time, count) VALUES(\'conns\', UNIX_TIMESTAMP(), 0),(\'users\', UNIX_TIMESTAMP(), 0);\" > /dev/null' % rExtra)
                #last one is to prevent an xc vulnerability, run "UPDATE settings SET get_real_ip_client='HTTP_CF_CONNECTING_IP' where id=1;" query if you are using cf proxy.
                os.system('mysql -u root%s -e "USE xtream_iptvpro; UPDATE settings SET get_real_ip_client=\'\', double_auth=\'1\', hash_lb=\'1\', mag_security=\'1\' where id=\'1\';" > /dev/null'  % rExtra)
                if not os.path.exists("/etc/mysql/mysqld"):
                    if not "EnvironmentFile=-/etc/mysql/mysqld" in open("/lib/systemd/system/mysql.service").read(): 
                        os.system('echo "LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.1" > /etc/mysql/mysqld')
                        os.system('echo "%s" > /lib/systemd/system/mysql.service' % rMySQLServiceFile)
                        os.system('systemctl daemon-reload; systemctl restart mysql.service;')
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
    rf.write(''.join(chr(ord(c)^ord(k)) for c,k in izip('{\"host\":\"%s\",\"db_user\":\"%s\",\"db_pass\":\"%s\",\"db_name\":\"%s\",\"server_id\":\"%d\", \"db_port\":\"%d\", \"pconnect\":\"0\"}' % (rHost, rUsername, rPassword, rDatabase, rServerID, rPort), cycle('5709650b0d7806074842c6de575025b1'))).encode('base64').replace('\n', ''))
    rf.close()

def configure():
    printc("Configuring System")
    if not "/home/xtreamcodes/iptv_xtream_codes/" in open("/etc/fstab").read():
        rFile = open("/etc/fstab", "a")
        rFile.write("tmpfs /home/xtreamcodes/iptv_xtream_codes/streams tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777,size=90% 0 0\ntmpfs /home/xtreamcodes/iptv_xtream_codes/tmp tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777,size=3G 0 0")
        rFile.close()
    if not "xtreamcodes" in open("/etc/sudoers").read():
        os.system('echo "xtreamcodes ALL = (root) NOPASSWD: /sbin/iptables, /usr/bin/chattr" >> /etc/sudoers')
    if not os.path.exists("/etc/init.d/xtreamcodes"):
        rFile = open("/etc/init.d/xtreamcodes", "w")
        rFile.write("#! /bin/bash\n/home/xtreamcodes/iptv_xtream_codes/start_services.sh")
        rFile.close()
        os.system("chmod +x /etc/init.d/xtreamcodes > /dev/null")
    os.system("mount -a")
    try: os.remove("/usr/bin/ffmpeg")
    except: pass
    if not os.path.exists("/home/xtreamcodes/iptv_xtream_codes/tv_archive"): os.mkdir("/home/xtreamcodes/iptv_xtream_codes/tv_archive/")
    os.system("ln -s /home/xtreamcodes/iptv_xtream_codes/bin/ffmpeg /usr/bin/")
    os.system("chown xtreamcodes:xtreamcodes -R /home/xtreamcodes > /dev/null")
    os.system("chmod -R 0777 /home/xtreamcodes > /dev/null")
    if rType == "MAIN": 
        os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/admin/ -type f -exec chmod 644 {} \;")
        os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/admin/ -type d -exec chmod 755 {} \;")
    os.system("wget -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/nginx -O /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx")
    os.system("wget -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/nginx_rtmp -O /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/sbin/nginx_rtmp")
    os.system("wget -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/pid_monitor.php -O /home/xtreamcodes/iptv_xtream_codes/crons/pid_monitor.php")
    os.system("sudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx")
    os.system("sudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/sbin/nginx_rtmp")
    os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/wwwdir/ -type f -exec chmod 644 {} \;")
    os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/wwwdir/ -type d -exec chmod 755 {} \;")
    os.system("chmod 0700 /home/xtreamcodes/iptv_xtream_codes/config > /dev/null")
    os.system("sed -i 's|echo \"Xtream Codes Reborn\";|header(\"Location: https://www.google.com/\");|g' /home/xtreamcodes/iptv_xtream_codes/wwwdir/index.php")
    os.system("wget -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/GeoLite2.mmdb -O /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb")
    os.system('chattr -f +i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null')
    os.system("sed -i 's|chown -R xtreamcodes:xtreamcodes /home/xtreamcodes|chown -R xtreamcodes:xtreamcodes /home/xtreamcodes 2>/dev/null|g' /home/xtreamcodes/iptv_xtream_codes/start_services.sh")
    os.system("chmod +x /home/xtreamcodes/iptv_xtream_codes/start_services.sh > /dev/null")

    if not "api.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    api.xtream-codes.com" >> /etc/hosts')
    if not "downloads.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    downloads.xtream-codes.com" >> /etc/hosts')
    if not "xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    xtream-codes.com" >> /etc/hosts')
    if not "@reboot root /home/xtreamcodes/iptv_xtream_codes/start_services.sh" in open("/etc/crontab").read(): os.system('echo "@reboot root /home/xtreamcodes/iptv_xtream_codes/start_services.sh" >> /etc/crontab')

def start(first=True):
    if first: printc("Starting Xtream Codes")
    else: printc("Restarting Xtream Codes")
    os.system("/home/xtreamcodes/iptv_xtream_codes/start_services.sh > /dev/null")


if __name__ == "__main__":

    try: rVersion = os.popen('lsb_release -sr').read().strip()
    except: rVersion = None
    if not rVersion in rVersions:
        printc("Unsupported Operating System, Works only on Ubuntu Server 16 and 18")
        sys.exit(1)

    printc("Xtream UI - Installer Mirror", col.OKGREEN, 2)
    print "%s │ Check out the mirror repo: https://bitbucket.org/emre1393/xtreamui_mirror %s" % (col.OKGREEN, col.ENDC)
    print " "
    rType = raw_input("  Installation Type [MAIN, LB]: ")
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
            rAccesscode = generate(12)

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
                if rType.upper() == "MAIN": 
                    installadminpanel()
                    os.system("sed -i 's|randomcodehere|%s|g' /home/xtreamcodes/iptv_xtream_codes/nginx/conf/admin_panel.conf" % rAccesscode)
                configure()
                start()
                printc("Installation completed!", col.OKGREEN, 2)
                if rType.upper() == "MAIN":
                    printc("Please store your MySQL password!")
                    printc(rPassword)
                    printc("Admin UI Login URL is:")
                    printc("http://%s:8080/%s" % (getIP(), rAccesscode))
                    printc("Admin UI default login is admin/admin")
            else: printc("Installation cancelled", col.FAIL)
        else: printc("Invalid entries", col.FAIL)
    else: printc("Invalid installation type", col.FAIL)
