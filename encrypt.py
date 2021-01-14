# -*- coding: utf-8 -*-
import subprocess, os, random, string, sys, shutil, socket, zipfile, urllib.request, urllib.error, urllib.parse, json, base64
from itertools import cycle
from zipfile import ZipFile
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


rServerID=1
rHost='127.0.0.1'
rPort=7999
rUsername='user_iptvpro'
rPassword='Tn0tPIbMnqL6FDUV'
rDatabase='xtream_iptvpro'

rf = open('./config', 'wb')

lestring=''.join(chr(ord(c)^ord(k)) for c,k in zip('{\"host\":\"%s\",\"db_user\":\"%s\",\"db_pass\":\"%s\",\"db_name\":\"%s\",\"server_id\":\"%d\", \"db_port\":\"%d\"}' % (rHost, rUsername, rPassword, rDatabase, rServerID, rPort), cycle('5709650b0d7806074842c6de575025b1')))

rf.write(base64.b64encode(bytes(lestring, 'ascii')))
rf.close()