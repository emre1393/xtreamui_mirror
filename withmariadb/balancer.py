#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, os, sys
from itertools import cycle, izip

rDownloadURL = "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/LB.tar.gz"
rPackages = ["libcurl3", "libxslt1-dev", "libgeoip-dev", "e2fsprogs", "wget", "mcrypt", "nscd", "htop", "zip", "unzip", "mc"]

rSysctlFile = "bmV0LmlwdjQudGNwX2Nvbmdlc3Rpb25fY29udHJvbCA9IGJicgpuZXQuY29yZS5kZWZhdWx0X3FkaXNjID0gZnEKbmV0LmlwdjQudGNwX3JtZW0gPSA4MTkyIDg3MzgwIDEzNDIxNzcyOApuZXQuaXB2NC51ZHBfcm1lbV9taW4gPSAxNjM4NApuZXQuY29yZS5ybWVtX2RlZmF1bHQgPSAyNjIxNDQKbmV0LmNvcmUucm1lbV9tYXggPSAyNjg0MzU0NTYKbmV0LmlwdjQudGNwX3dtZW0gPSA4MTkyIDY1NTM2IDEzNDIxNzcyOApuZXQuaXB2NC51ZHBfd21lbV9taW4gPSAxNjM4NApuZXQuY29yZS53bWVtX2RlZmF1bHQgPSAyNjIxNDQKbmV0LmNvcmUud21lbV9tYXggPSAyNjg0MzU0NTYKbmV0LmNvcmUuc29tYXhjb25uID0gMTAwMDAwMApuZXQuY29yZS5uZXRkZXZfbWF4X2JhY2tsb2cgPSAyNTAwMDAKbmV0LmNvcmUub3B0bWVtX21heCA9IDY1NTM1Cm5ldC5pcHY0LnRjcF9tYXhfdHdfYnVja2V0cyA9IDE0NDAwMDAKbmV0LmlwdjQudGNwX21heF9vcnBoYW5zID0gMTYzODQKbmV0LmlwdjQuaXBfbG9jYWxfcG9ydF9yYW5nZSA9IDIwMDAgNjUwMDAKbmV0LmlwdjQudGNwX25vX21ldHJpY3Nfc2F2ZSA9IDEKbmV0LmlwdjQudGNwX3Nsb3dfc3RhcnRfYWZ0ZXJfaWRsZSA9IDAKbmV0LmlwdjQudGNwX2Zpbl90aW1lb3V0ID0gMTUKbmV0LmlwdjQudGNwX2tlZXBhbGl2ZV90aW1lID0gMzAwCm5ldC5pcHY0LnRjcF9rZWVwYWxpdmVfcHJvYmVzID0gNQpuZXQuaXB2NC50Y3Bfa2VlcGFsaXZlX2ludHZsID0gMTUKZnMuZmlsZS1tYXg9MjA5NzA4MDAKZnMubnJfb3Blbj0yMDk3MDgwMApmcy5haW8tbWF4LW5yPTIwOTcwODAwCm5ldC5pcHY0LnRjcF90aW1lc3RhbXBzID0gMQpuZXQuaXB2NC50Y3Bfd2luZG93X3NjYWxpbmcgPSAxCm5ldC5pcHY0LnRjcF9tdHVfcHJvYmluZyA9IDEKbmV0LmlwdjQucm91dGUuZmx1c2ggPSAxCm5ldC5pcHY2LnJvdXRlLmZsdXNoID0gMQ==".decode("base64")
rXCserviceFile = "IyEvYmluL2Jhc2gKClNDUklQVD0vaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2RlcwpVU0VSPSQod2hvYW1pKQoKaWYgW1sgJFVTRVIgIT0gInJvb3QiIF1dOyB0aGVuCiAgZWNobyAiUGxlYXNlIHJ1biBhcyByb290ISIKICBleGl0IDAKZmkKCnN0YXJ0KCkgewogIHBpZHM9JChwZ3JlcCAtdSB4dHJlYW1jb2RlcyBuZ2lueCB8IHdjIC1sKQogIGlmIFsgJHBpZHMgIT0gMCBdOyB0aGVuCiAgICBlY2hvICd4dHJlYW1jb2RlcyBpcyBhbHJlYWR5IHJ1bm5pbmcnCiAgICByZXR1cm4gMQogIGZpCiAgZWNobyAnU3RhcnRpbmcgeHRyZWFtY29kZXMuLi4nCgogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMgoKICBzdWRvIC11IHh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9iaW4vcGhwIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL2Nyb25zL3NldHVwX2NhY2hlLnBocAogIHN1ZG8gLXUgeHRyZWFtY29kZXMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2Jpbi9waHAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvdG9vbHMvc2lnbmFsX3JlY2VpdmVyLnBocCA+L2Rldi9udWxsIDI+L2Rldi9udWxsICYKICBzdWRvIC11IHh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9iaW4vcGhwIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3Rvb2xzL3BpcGVfcmVhZGVyLnBocCA+L2Rldi9udWxsIDI+L2Rldi9udWxsICYKICBjaG93biAtUiB4dHJlYW1jb2Rlczp4dHJlYW1jb2RlcyAvc3lzL2NsYXNzL25ldAogIGNob3duIC1SIHh0cmVhbWNvZGVzOnh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzID4vZGV2L251bGwgMj4vZGV2L251bGwKICBzbGVlcCAxCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMS5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMS5jb25mCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMi5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMi5jb25mCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMy5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMy5jb25mCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvNC5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvNC5jb25mCiAgc2xlZXAgMwogIGNobW9kICt4IC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54X3J0bXAvc2Jpbi9uZ2lueF9ydG1wCiAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbnhfcnRtcC9zYmluL25naW54X3J0bXAKICBzbGVlcCAxCiAgY2htb2QgK3ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbngvc2Jpbi9uZ2lueAogIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54L3NiaW4vbmdpbngKICBlY2hvICdSdW5uaW5nIGluIGZvcmVncm91bmQuLi4nCiAgc2xlZXAgaW5maW5pdHkKfQoKc3RvcCgpIHsKICBwaWRzPSQocGdyZXAgLXUgeHRyZWFtY29kZXMgbmdpbnggfCB3YyAtbCkKICBpZiBbWyAkcGlkcyA9IDAgXV07IHRoZW4KICAgIGVjaG8gJ3h0cmVhbWNvZGVzIGlzIG5vdCBydW5uaW5nJwogICAgcmV0dXJuIDEKICBmaQogIGVjaG8gJ1N0b3BwaW5nIHh0cmVhbWNvZGVzLi4uJwogIHN1ZG8ga2lsbGFsbCAtdSB4dHJlYW1jb2RlcwogIHNsZWVwIDEKICBzdWRvIGtpbGxhbGwgLXUgeHRyZWFtY29kZXMKICBzbGVlcCAxCiAgc3VkbyBraWxsYWxsIC11IHh0cmVhbWNvZGVzCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMgoKfQoKcmVzdGFydCgpIHsKICBzdG9wCiAgI3BzIC1VIHh0cmVhbWNvZGVzIHwgZWdyZXAgLXYgImZmbXBlZ3xQSUQiIHwgYXdrICd7cHJpbnQgJDF9JyB8IHhhcmdzIGtpbGwgLTkKICBzdGFydAp9CgpyZWxvYWQoKSB7CiAgcGlkcz0kKHBncmVwIC11IHh0cmVhbWNvZGVzIG5naW54IHwgd2MgLWwpCiAgaWYgW1sgJHBpZHMgPSAwIF1dOyB0aGVuCiAgICBlY2hvICd4dHJlYW1jb2RlcyBuZ2lueCBpcyBub3QgcnVubmluZycKICAgIHJldHVybiAxCiAgZmkKICBlY2hvICdSZWxvYWRpbmcgbmdpbnggY29uZmlnIGZvciB4dHJlYW1jb2Rlcy4uLicKICAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9uZ2lueC9zYmluL25naW54IC1zIHJlbG9hZAogIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54X3J0bXAvc2Jpbi9uZ2lueF9ydG1wIC1zIHJlbG9hZAp9CgpjYXNlICIkMSIgaW4KICBzdGFydCkKICAgIHN0YXJ0CiAgICA7OwogIHN0b3ApCiAgICBzdG9wCiAgICA7OwogIHJlbG9hZCkKICAgIHJlbG9hZAogICAgOzsKICByZXN0YXJ0KQogICAgcmVzdGFydAogICAgOzsKICAqKQogICAgZWNobyAiVXNhZ2U6ICQwIHtzdGFydHxzdG9wfHJlc3RhcnR8cmVsb2FkfSIKZXNhYwoKZXhpdCAw==".decode("base64")
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
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/GeoLite2.mmdb -O /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/pid_monitor.php -O /home/xtreamcodes/iptv_xtream_codes/crons/pid_monitor.php")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/nginx -O /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/nginx_rtmp -O /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx_rtmp")
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
    if not "xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    xtream-codes.com" >> /etc/hosts')
    if not "api.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    api.xtream-codes.com" >> /etc/hosts')
    if not "downloads.xtream-codes.com" in open("/etc/hosts").read(): os.system('echo "127.0.0.1    downloads.xtream-codes.com" >> /etc/hosts')
    #adds domain/user/pass/id.ts url support
    with open('/home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf', 'r') as nginx_file:
        nginx_replace = nginx_file.read()
        nginx_replace = nginx_replace.replace("rewrite ^/(.*)/(.*)/(\\d+)$ /streaming/clients_live.php?username=$1&password=$2&stream=$3&extension=ts break;", "rewrite ^/(.*)/(.*)/(\\d+)\\.(.*)$ /streaming/clients_live.php?username=$1&password=$2&stream=$3&extension=$4 break;\r\n        rewrite ^/(.*)/(.*)/(\\d+)$ /streaming/clients_live.php?username=$1&password=$2&stream=$3&extension=ts break;\r\n")
    with open('/home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf', 'w') as nginx_file:
        nginx_file.write(nginx_replace)



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
