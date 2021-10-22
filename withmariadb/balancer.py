#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, os, sys
from itertools import cycle, izip

rDownloadURL = "https://bitbucket.org/emre1393/xtreamui_mirror/downloads/sub_xtreamcodes_reborn.tar.gz"
rPackages = ["libcurl3", "libxslt1-dev", "libgeoip-dev", "e2fsprogs", "wget", "mcrypt", "nscd", "htop", "zip", "unzip", "mc"]

rSysctlFile = "bmV0LmlwdjQudGNwX2Nvbmdlc3Rpb25fY29udHJvbCA9IGJicgpuZXQuY29yZS5kZWZhdWx0X3FkaXNjID0gZnEKbmV0LmlwdjQudGNwX3JtZW0gPSA4MTkyIDg3MzgwIDEzNDIxNzcyOApuZXQuaXB2NC51ZHBfcm1lbV9taW4gPSAxNjM4NApuZXQuY29yZS5ybWVtX2RlZmF1bHQgPSAyNjIxNDQKbmV0LmNvcmUucm1lbV9tYXggPSAyNjg0MzU0NTYKbmV0LmlwdjQudGNwX3dtZW0gPSA4MTkyIDY1NTM2IDEzNDIxNzcyOApuZXQuaXB2NC51ZHBfd21lbV9taW4gPSAxNjM4NApuZXQuY29yZS53bWVtX2RlZmF1bHQgPSAyNjIxNDQKbmV0LmNvcmUud21lbV9tYXggPSAyNjg0MzU0NTYKbmV0LmNvcmUuc29tYXhjb25uID0gMTAwMDAwMApuZXQuY29yZS5uZXRkZXZfbWF4X2JhY2tsb2cgPSAyNTAwMDAKbmV0LmNvcmUub3B0bWVtX21heCA9IDY1NTM1Cm5ldC5pcHY0LnRjcF9tYXhfdHdfYnVja2V0cyA9IDE0NDAwMDAKbmV0LmlwdjQudGNwX21heF9vcnBoYW5zID0gMTYzODQKbmV0LmlwdjQuaXBfbG9jYWxfcG9ydF9yYW5nZSA9IDIwMDAgNjUwMDAKbmV0LmlwdjQudGNwX25vX21ldHJpY3Nfc2F2ZSA9IDEKbmV0LmlwdjQudGNwX3Nsb3dfc3RhcnRfYWZ0ZXJfaWRsZSA9IDAKbmV0LmlwdjQudGNwX2Zpbl90aW1lb3V0ID0gMTUKbmV0LmlwdjQudGNwX2tlZXBhbGl2ZV90aW1lID0gMzAwCm5ldC5pcHY0LnRjcF9rZWVwYWxpdmVfcHJvYmVzID0gNQpuZXQuaXB2NC50Y3Bfa2VlcGFsaXZlX2ludHZsID0gMTUKZnMuZmlsZS1tYXg9MjA5NzA4MDAKZnMubnJfb3Blbj0yMDk3MDgwMApmcy5haW8tbWF4LW5yPTIwOTcwODAwCm5ldC5pcHY0LnRjcF90aW1lc3RhbXBzID0gMQpuZXQuaXB2NC50Y3Bfd2luZG93X3NjYWxpbmcgPSAxCm5ldC5pcHY0LnRjcF9tdHVfcHJvYmluZyA9IDEKbmV0LmlwdjQucm91dGUuZmx1c2ggPSAxCm5ldC5pcHY2LnJvdXRlLmZsdXNoID0gMQ==".decode("base64")
rXCserviceFile = "IyEvYmluL3NoCgpTQ1JJUFQ9L2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMKVVNFUj0kKHdob2FtaSkKCmlmIFtbICRVU0VSICE9ICJyb290IiBdXTsgdGhlbgogIGVjaG8gIlBsZWFzZSBydW4gYXMgcm9vdCEiCiAgZXhpdCAwCmZpCgpzdGFydCgpIHsKICBwaWRzPSQocGdyZXAgLXUgeHRyZWFtY29kZXMgbmdpbnggfCB3YyAtbCkKICBpZiBbICRwaWRzICE9IDAgXTsgdGhlbgogICAgZWNobyAneHRyZWFtY29kZXMgaXMgYWxyZWFkeSBydW5uaW5nJwogICAgcmV0dXJuIDEKICBmaQogIGVjaG8gJ1N0YXJ0aW5nIHh0cmVhbWNvZGVzLi4uJwoKICBraWxsICQocHMgYXV4IHwgZ3JlcCAneHRyZWFtY29kZXMnIHwgZ3JlcCAtdiBncmVwIHwgZ3JlcCAtdiAnL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZScgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbAogIHNsZWVwIDEKICBraWxsICQocHMgYXV4IHwgZ3JlcCAneHRyZWFtY29kZXMnIHwgZ3JlcCAtdiBncmVwIHwgZ3JlcCAtdiAnL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZScgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbAogIHNsZWVwIDEKICBraWxsICQocHMgYXV4IHwgZ3JlcCAneHRyZWFtY29kZXMnIHwgZ3JlcCAtdiBncmVwIHwgZ3JlcCAtdiAnL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZScgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbAogIHNsZWVwIDIKCiAgc3VkbyAtdSB4dHJlYW1jb2RlcyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvYmluL3BocCAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9jcm9ucy9zZXR1cF9jYWNoZS5waHAKICBzdWRvIC11IHh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9iaW4vcGhwIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3Rvb2xzL3NpZ25hbF9yZWNlaXZlci5waHAgPi9kZXYvbnVsbCAyPi9kZXYvbnVsbCAmCiAgc3VkbyAtdSB4dHJlYW1jb2RlcyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvYmluL3BocCAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy90b29scy9waXBlX3JlYWRlci5waHAgPi9kZXYvbnVsbCAyPi9kZXYvbnVsbCAmCiAgY2hvd24gLVIgeHRyZWFtY29kZXM6eHRyZWFtY29kZXMgL3N5cy9jbGFzcy9uZXQKICBjaG93biAtUiB4dHJlYW1jb2Rlczp4dHJlYW1jb2RlcyAvaG9tZS94dHJlYW1jb2RlcyA+L2Rldi9udWxsIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIHN0YXJ0LXN0b3AtZGFlbW9uIC0tc3RhcnQgLS1xdWlldCAtLXBpZGZpbGUgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzEucGlkIC0tZXhlYyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvc2Jpbi9waHAtZnBtIC0tIC0tZGFlbW9uaXplIC0tZnBtLWNvbmZpZyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvZXRjLzEuY29uZgogIHN0YXJ0LXN0b3AtZGFlbW9uIC0tc3RhcnQgLS1xdWlldCAtLXBpZGZpbGUgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzIucGlkIC0tZXhlYyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvc2Jpbi9waHAtZnBtIC0tIC0tZGFlbW9uaXplIC0tZnBtLWNvbmZpZyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvZXRjLzIuY29uZgogIHN0YXJ0LXN0b3AtZGFlbW9uIC0tc3RhcnQgLS1xdWlldCAtLXBpZGZpbGUgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzMucGlkIC0tZXhlYyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvc2Jpbi9waHAtZnBtIC0tIC0tZGFlbW9uaXplIC0tZnBtLWNvbmZpZyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvZXRjLzMuY29uZgogIHN0YXJ0LXN0b3AtZGFlbW9uIC0tc3RhcnQgLS1xdWlldCAtLXBpZGZpbGUgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzQucGlkIC0tZXhlYyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvc2Jpbi9waHAtZnBtIC0tIC0tZGFlbW9uaXplIC0tZnBtLWNvbmZpZyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvZXRjLzQuY29uZgogIHNsZWVwIDMKICBjaG1vZCAreCAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9uZ2lueF9ydG1wL3NiaW4vbmdpbnhfcnRtcAogIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54X3J0bXAvc2Jpbi9uZ2lueF9ydG1wCiAgc2xlZXAgMQogIGNobW9kICt4IC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54L3NiaW4vbmdpbngKICAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9uZ2lueC9zYmluL25naW54CiAgZWNobyAnUnVubmluZyBpbiBmb3JlZ3JvdW5kLi4uJwogIHNsZWVwIGluZmluaXR5Cn0KCnN0b3AoKSB7CiAgcGlkcz0kKHBncmVwIC11IHh0cmVhbWNvZGVzIG5naW54IHwgd2MgLWwpCiAgaWYgW1sgJHBpZHMgPSAwIF1dOyB0aGVuCiAgICBlY2hvICd4dHJlYW1jb2RlcyBpcyBub3QgcnVubmluZycKICAgIHJldHVybiAxCiAgZmkKICBlY2hvICdTdG9wcGluZyB4dHJlYW1jb2Rlcy4uLicKICBzdWRvIGtpbGxhbGwgLXUgeHRyZWFtY29kZXMKICBzbGVlcCAxCiAgc3VkbyBraWxsYWxsIC11IHh0cmVhbWNvZGVzCiAgc2xlZXAgMQogIHN1ZG8ga2lsbGFsbCAtdSB4dHJlYW1jb2RlcwogIHNsZWVwIDEKICBraWxsICQocHMgYXV4IHwgZ3JlcCAneHRyZWFtY29kZXMnIHwgZ3JlcCAtdiBncmVwIHwgZ3JlcCAtdiAnL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZScgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbAogIHNsZWVwIDEKICBraWxsICQocHMgYXV4IHwgZ3JlcCAneHRyZWFtY29kZXMnIHwgZ3JlcCAtdiBncmVwIHwgZ3JlcCAtdiAnL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZScgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbAogIHNsZWVwIDEKICBraWxsICQocHMgYXV4IHwgZ3JlcCAneHRyZWFtY29kZXMnIHwgZ3JlcCAtdiBncmVwIHwgZ3JlcCAtdiAnL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZScgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbAogIHNsZWVwIDIKCn0KCnJlc3RhcnQoKSB7CiAgc3RvcAogICNwcyAtVSB4dHJlYW1jb2RlcyB8IGVncmVwIC12ICJmZm1wZWd8UElEIiB8IGF3ayAne3ByaW50ICQxfScgfCB4YXJncyBraWxsIC05CiAgc3RhcnQKfQoKcmVsb2FkKCkgewogIHBpZHM9JChwZ3JlcCAtdSB4dHJlYW1jb2RlcyBuZ2lueCB8IHdjIC1sKQogIGlmIFtbICRwaWRzID0gMCBdXTsgdGhlbgogICAgZWNobyAneHRyZWFtY29kZXMgbmdpbnggaXMgbm90IHJ1bm5pbmcnCiAgICByZXR1cm4gMQogIGZpCiAgZWNobyAnUmVsb2FkaW5nIG5naW54IGNvbmZpZyBmb3IgeHRyZWFtY29kZXMuLi4nCiAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbngvc2Jpbi9uZ2lueCAtcyByZWxvYWQKICAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9uZ2lueF9ydG1wL3NiaW4vbmdpbnhfcnRtcCAtcyByZWxvYWQKfQoKY2FzZSAiJDEiIGluCiAgc3RhcnQpCiAgICBzdGFydAogICAgOzsKICBzdG9wKQogICAgc3RvcAogICAgOzsKICByZWxvYWQpCiAgICByZWxvYWQKICAgIDs7CiAgcmVzdGFydCkKICAgIHJlc3RhcnQKICAgIDs7CiAgKikKICAgIGVjaG8gIlVzYWdlOiAkMCB7c3RhcnR8c3RvcHxyZXN0YXJ0fHJlbG9hZH0iCmVzYWMKCmV4aXQgMA==".decode("base64")
rNewStartServices = "IyEgL2Jpbi9iYXNoCmtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICdzdGFydF9zZXJ2aWNlcy5zaCcgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbApzbGVlcCAxCmtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICdzdGFydF9zZXJ2aWNlcy5zaCcgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbApzbGVlcCAxCmtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICdzdGFydF9zZXJ2aWNlcy5zaCcgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbApzbGVlcCA0CnN1ZG8gLXUgeHRyZWFtY29kZXMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2Jpbi9waHAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvY3JvbnMvc2V0dXBfY2FjaGUucGhwCnN1ZG8gLXUgeHRyZWFtY29kZXMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2Jpbi9waHAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvdG9vbHMvc2lnbmFsX3JlY2VpdmVyLnBocCA+L2Rldi9udWxsIDI+L2Rldi9udWxsICYKc3VkbyAtdSB4dHJlYW1jb2RlcyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvYmluL3BocCAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy90b29scy9waXBlX3JlYWRlci5waHAgPi9kZXYvbnVsbCAyPi9kZXYvbnVsbCAmCmNob3duIC1SIHh0cmVhbWNvZGVzOnh0cmVhbWNvZGVzIC9zeXMvY2xhc3MvbmV0CmNob3duIC1SIHh0cmVhbWNvZGVzOnh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzICA+L2Rldi9udWxsIDI+L2Rldi9udWxsCnNsZWVwIDQKY2htb2QgK3ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbnhfcnRtcC9zYmluL25naW54X3J0bXAKY2htb2QgK3ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvL25naW54L3NiaW4vbmdpbngKL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbnhfcnRtcC9zYmluL25naW54X3J0bXAKL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbngvc2Jpbi9uZ2lueApzdGFydC1zdG9wLWRhZW1vbiAtLXN0YXJ0IC0tcXVpZXQgLS1waWRmaWxlIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC8xLnBpZCAtLWV4ZWMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL3NiaW4vcGhwLWZwbSAtLSAtLWRhZW1vbml6ZSAtLWZwbS1jb25maWcgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2V0Yy8xLmNvbmYKc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMi5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMi5jb25mCnN0YXJ0LXN0b3AtZGFlbW9uIC0tc3RhcnQgLS1xdWlldCAtLXBpZGZpbGUgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzMucGlkIC0tZXhlYyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvc2Jpbi9waHAtZnBtIC0tIC0tZGFlbW9uaXplIC0tZnBtLWNvbmZpZyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvZXRjLzMuY29uZgpzdGFydC1zdG9wLWRhZW1vbiAtLXN0YXJ0IC0tcXVpZXQgLS1waWRmaWxlIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC80LnBpZCAtLWV4ZWMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL3NiaW4vcGhwLWZwbSAtLSAtLWRhZW1vbml6ZSAtLWZwbS1jb25maWcgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2V0Yy80LmNvbmYKIA==".decode("base64")
rSystemdUnitFile = "=W1VuaXRdClNvdXJjZVBhdGg9L2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZQpEZXNjcmlwdGlvbj14dHJlYW1jb2RlcyBzZXJ2aWNlCkFmdGVyPW5ldHdvcmsudGFyZ2V0ClN0YXJ0TGltaXRJbnRlcnZhbFNlYz0wCiAKW1NlcnZpY2VdClR5cGU9c2ltcGxlClVzZXI9cm9vdApSZXN0YXJ0PW9uLWZhaWx1cmUKUmVzdGFydFNlYz01CkV4ZWNTdGFydD0vYmluL2Jhc2ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZSBzdGFydApFeGVjUmVzdGFydD0vYmluL2Jhc2ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZSByZXN0YXJ0CkV4ZWNTdG9wPS9iaW4vYmFzaCAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlIHN0b3AKRXhlY1JlbG9hZD0vYmluL2Jhc2ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZSByZWxvYWQKIApbSW5zdGFsbF0KV2FudGVkQnk9bXVsdGktdXNlci50YXJnZXQ==".decode("base64")
rNginxBalanceFile = "dXBzdHJlYW0gcGhwIHsKICAgIGxlYXN0X2Nvbm47CiAgICBzZXJ2ZXIgdW5peDovaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMS5zb2NrOwogICAgc2VydmVyIHVuaXg6L2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzIuc29jazsKICAgIHNlcnZlciB1bml4Oi9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC8zLnNvY2s7CiAgICBzZXJ2ZXIgdW5peDovaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvNC5zb2NrOwp9Cg==".decode("base64")
rPhpfpm1 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzEucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMS5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")
rPhpfpm2 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzIucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMi5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")
rPhpfpm3 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzMucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMy5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")
rPhpfpm4 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzQucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvNC5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")

def getVersion():
    try: return subprocess.check_output("lsb_release -d".split()).split(":")[-1].strip()
    except: return ""

def prepare():
    global rPackages
    for rFile in ["/var/lib/dpkg/lock-frontend", "/var/cache/apt/archives/lock", "/var/lib/dpkg/lock"]:
        try: os.remove(rFile)
        except: pass
    os.system("apt-get update > /dev/null")
    os.system("apt-get remove --auto-remove libcurl4 -y > /dev/null")
    os.system("sudo apt -y install snapd")
    os.system("snap install curl > /dev/null")
    for rPackage in rPackages: os.system("apt-get install %s -y > /dev/null" % rPackage)
    os.system("wget --user-agent=\"Mozilla/5.0\" -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb")
    os.system("dpkg -i /tmp/libpng12.deb > /dev/null")
    os.system("apt-get install -y > /dev/null") # Clean up above
    try: os.remove("/tmp/libpng12.deb")
    except: pass
    os.system("adduser --system --shell /bin/false --group --disabled-login xtreamcodes > /dev/null")
    if not os.path.exists("/home/xtreamcodes"): os.mkdir("/home/xtreamcodes")
    return True

def install():
    global rDownloadURL
    rURL = rDownloadURL
    if os.path.exists("/home/xtreamcodes"):
        if os.path.exists("/etc/systemd/system/xtreamcodes.service"):
            os.system("systemctl stop xtreamcodes")
        else:
            os.system("kill $(ps aux | grep '[p]hp' | awk '{print $2}')")
            os.system("kill $(ps aux | grep '[n]nginx' | awk '{print $2}')")
            os.system("kill $(ps aux | grep '[f]fmpeg' | awk '{print $2}')")
        os.system("chattr -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null")
        os.system("rm -rf /home/xtreamcodes/tmp/* > /dev/null")
        os.system("rm -rf /home/xtreamcodes/streams/* > /dev/null")
    os.system('wget --user-agent="Mozilla/5.0" -q -O "/tmp/xtreamcodes.tar.gz" "%s"' % rURL)
    if os.path.exists("/tmp/xtreamcodes.tar.gz"):
        os.system('tar -zxvf "/tmp/xtreamcodes.tar.gz" -C "/home/xtreamcodes/" > /dev/null')
        try: os.remove("/tmp/xtreamcodes.tar.gz")
        except: pass
        return True
    return False

def encrypt(rHost="127.0.0.1", rUsername="user_iptvpro", rPassword="", rDatabase="xtream_iptvpro", rServerID=1, rPort=7999):
    try: os.remove("/home/xtreamcodes/iptv_xtream_codes/config")
    except: pass
    rf = open('/home/xtreamcodes/iptv_xtream_codes/config', 'wb')
    rf.write(''.join(chr(ord(c)^ord(k)) for c,k in izip('{\"host\":\"%s\",\"db_user\":\"%s\",\"db_pass\":\"%s\",\"db_name\":\"%s\",\"server_id\":\"%d\", \"db_port\":\"%d\", \"pconnect\":\"0\"}' % (rHost, rUsername, rPassword, rDatabase, rServerID, rPort), cycle('5709650b0d7806074842c6de575025b1'))).encode('base64').replace('\n', ''))
    rf.close()

def configure():
    if not "/home/xtreamcodes/iptv_xtream_codes/" in open("/etc/fstab").read():
        rFile = open("/etc/fstab", "a")
        rFile.write("tmpfs /home/xtreamcodes/iptv_xtream_codes/streams tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777,size=90% 0 0\ntmpfs /home/xtreamcodes/iptv_xtream_codes/tmp tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777,size=2G 0 0")
        rFile.close()
    if not "xtreamcodes" in open("/etc/sudoers").read(): os.system('echo "xtreamcodes ALL = (root) NOPASSWD: /sbin/iptables" >> /etc/sudoers')
    try: os.remove("/usr/bin/ffmpeg")
    except: pass
    if not os.path.exists("/home/xtreamcodes/iptv_xtream_codes/tv_archive"): os.mkdir("/home/xtreamcodes/iptv_xtream_codes/tv_archive/")
    os.system("ln -s /home/xtreamcodes/iptv_xtream_codes/bin/ffmpeg /usr/bin/")
    os.system("chattr -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null")
    os.system("chmod -R 0777 /home/xtreamcodes > /dev/null")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/GeoLite2.mmdb -O /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/pid_monitor.php -O /home/xtreamcodes/iptv_xtream_codes/crons/pid_monitor.php")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/nginx -O /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://bitbucket.org/emre1393/xtreamui_mirror/downloads/nginx_rtmp -O /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx_rtmp")
    os.system("sudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx")
    os.system("sudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/sbin/nginx_rtmp")
    os.system("mount -a")
    os.system("chmod 0700 /home/xtreamcodes/iptv_xtream_codes/config > /dev/null")
    os.system("sed -i 's|echo \"Xtream Codes Reborn\";|header(\"Location: https://www.google.com/\");|g' /home/xtreamcodes/iptv_xtream_codes/wwwdir/index.php")
    os.system("wget --user-agent=\"Mozilla/5.0\"  -q https://yt-dl.org/downloads/latest/youtube-dl -O /home/xtreamcodes/iptv_xtream_codes/bin/youtube")
    os.system("chmod a+rx /home/xtreamcodes/iptv_xtream_codes/bin/youtube")
    os.system('echo "%s" > /home/xtreamcodes/iptv_xtream_codes/nginx/conf/balance.conf' % rNginxBalanceFile)
    os.system("rm /home/xtreamcodes/iptv_xtream_codes/php/etc/*.conf")
    os.system('echo "%s" > /home/xtreamcodes/iptv_xtream_codes/php/etc/1.conf' % rPhpfpm1)
    os.system('echo "%s" > /home/xtreamcodes/iptv_xtream_codes/php/etc/2.conf' % rPhpfpm2)
    os.system('echo "%s" > /home/xtreamcodes/iptv_xtream_codes/php/etc/3.conf' % rPhpfpm3)
    os.system('echo "%s" > /home/xtreamcodes/iptv_xtream_codes/php/etc/4.conf' % rPhpfpm4)
    if os.path.exists("/etc/sysctl.conf"):
        os.system("cp /etc/sysctl.conf /etc/sysctl.conf.bak")
    os.system('echo "%s" > /etc/sysctl.conf' % rSysctlFile)
    os.system("sudo sysctl -p >/dev/null 2>&1")
    if not "DefaultLimitNOFILE=655350" in open("/etc/systemd/system.conf").read():
        os.system('sudo echo "DefaultLimitNOFILE=655350" >> "/etc/systemd/system.conf"')
        os.system('sudo echo "DefaultLimitNOFILE=655350" >> "/etc/systemd/user.conf"')
    if os.path.exists("/home/xtreamcodes/iptv_xtream_codes/service"):
        os.remove("/home/xtreamcodes/iptv_xtream_codes/service")
    rFile = open("/home/xtreamcodes/iptv_xtream_codes/service", "w")
    rFile.write(rXCserviceFile)
    rFile.close()
    os.system("chmod +x /home/xtreamcodes/iptv_xtream_codes/service > /dev/null")
    if os.path.exists("/home/xtreamcodes/iptv_xtream_codes/start_services.sh"):
        os.remove("/home/xtreamcodes/iptv_xtream_codes/start_services.sh")
    rFile = open("/home/xtreamcodes/iptv_xtream_codes/start_services.sh", "w")
    rFile.write(rNewStartServices)
    rFile.close()
    os.system("chmod +x /home/xtreamcodes/iptv_xtream_codes/start_services.sh > /dev/null")
    if os.path.exists("/etc/init.d/xtreamcodes"): os.remove("/etc/init.d/xtreamcodes")
    if os.path.exists("/etc/systemd/system/xtreamcodes.service"): os.remove("/etc/systemd/system/xtreamcodes.service")
    if not os.path.exists("/etc/systemd/system/xtreamcodes.service"):
        rFile = open("/etc/systemd/system/xtreamcodes.service", "w")
        rFile.write(rSystemdUnitFile)
        rFile.close()
    os.system("sudo chmod +x /etc/systemd/system/xtreamcodes.service")
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable xtreamcodes")
    os.system("chown xtreamcodes:xtreamcodes -R /home/xtreamcodes > /dev/null")
    os.system('chattr -f +i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null')
    if not "api.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    api.xtream-codes.com" >> /etc/hosts')
    if not "downloads.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    downloads.xtream-codes.com" >> /etc/hosts')
    if not "xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    xtream-codes.com" >> /etc/hosts')



def start(): os.system("sudo systemctl start xtreamcodes")

def setPorts(rPorts):
    os.system("sed -i 's/listen 25461;/listen %d;/g' /home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf" % rPorts[0])
    os.system("sed -i 's/:25461/:%d/g' /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/conf/nginx.conf" % rPorts[0])
    os.system("sed -i 's/listen 25463 ssl;/listen %d ssl;/g' /home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf" % rPorts[1])
    os.system("sed -i 's/listen 25462;/listen %d;/g' /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/conf/nginx.conf" % rPorts[2])

if __name__ == "__main__":
    rHost = sys.argv[1]
    rPort = int(sys.argv[2])
    rUsername = sys.argv[3]
    rPassword = sys.argv[4]
    rDatabase = sys.argv[5]
    rServerID = int(sys.argv[6])
    try: rPorts = [int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])]
    except: rPorts = None
    rRet = prepare()
    if not install(): sys.exit(1)
    encrypt(rHost, rUsername, rPassword, rDatabase, rServerID, rPort)
    configure()
    if rPorts: setPorts(rPorts)
    start()
    
#13.03.2020 minimum R22B version is required for lb installation with custom ports.
