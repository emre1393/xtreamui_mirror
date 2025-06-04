#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, os, random, string, sys, shutil, socket, zipfile, time
from itertools import cycle, izip
from zipfile import ZipFile

rDownloadURL = {"main": "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/main.tar.gz", "sub": "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/LB.tar.gz"}
rPackages = ["libcurl3", "libxslt1-dev", "libgeoip-dev", "e2fsprogs", "wget", "mcrypt", "nscd", "htop", "zip", "unzip", "mc", "libjemalloc1", "python-paramiko", "mariadb-server"]
rInstall = {"MAIN": "main", "LB": "sub"}
rMySQLCnf = "IyBYdHJlYW0gQ29kZXMKW2NsaWVudF0KcG9ydCAgICAgICAgICAgICAgICAgICAgICAgICAgICA9IDMzMDYKCltteXNxbGRfc2FmZV0KbmljZSAgICAgICAgICAgICAgICAgICAgICAgICAgICA9IDAKI21hbGxvYyBzZXR0aW5ncwptYWxsb2MtbGliPS91c3IvbGliL3g4Nl82NC1saW51eC1nbnUvbGlidGNtYWxsb2Muc28uNC4zLjAKCltteXNxbGRdCnVzZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgPSBteXNxbApwb3J0ICAgICAgICAgICAgICAgICAgICAgICAgICAgID0gNzk5OQpiYXNlZGlyICAgICAgICAgICAgICAgICAgICAgICAgID0gL3VzcgpkYXRhZGlyICAgICAgICAgICAgICAgICAgICAgICAgID0gL3Zhci9saWIvbXlzcWwKdG1wZGlyICAgICAgICAgICAgICAgICAgICAgICAgICA9IC90bXAKbGMtbWVzc2FnZXMtZGlyICAgICAgICAgICAgICAgICA9IC91c3Ivc2hhcmUvbXlzcWwKc2tpcC1leHRlcm5hbC1sb2NraW5nCnNraXAtbmFtZS1yZXNvbHZlICAgICAgICAgICAgICAgPTEKYmluZC1hZGRyZXNzICAgICAgICAgICAgICAgICAgICA9ICoKCmtleV9idWZmZXJfc2l6ZSAgICAgICAgICAgICAgICAgPSAxMjhNCm15aXNhbV9zb3J0X2J1ZmZlcl9zaXplICAgICAgICAgPSA0TQptYXhfYWxsb3dlZF9wYWNrZXQgICAgICAgICAgICAgID0gNjRNCm15aXNhbS1yZWNvdmVyLW9wdGlvbnMgICAgICAgICAgPSBCQUNLVVAKbWF4X2xlbmd0aF9mb3Jfc29ydF9kYXRhICAgICAgICA9IDgxOTIKcXVlcnlfY2FjaGVfbGltaXQgICAgICAgICAgICAgICA9IDAKcXVlcnlfY2FjaGVfc2l6ZSAgICAgICAgICAgICAgICA9IDAKcXVlcnlfY2FjaGVfdHlwZSAgICAgICAgICAgICAgICA9IDAKZXhwaXJlX2xvZ3NfZGF5cyAgICAgICAgICAgICAgICA9IDEwCm1heF9iaW5sb2dfc2l6ZSAgICAgICAgICAgICAgICAgPSAxMDBNCm1heF9jb25uZWN0aW9ucyAgICAgICAgICAgICAgICAgPSA4MTkyCmJhY2tfbG9nICAgICAgICAgICAgICAgICAgICAgICAgPSA0MDk2Cm9wZW5fZmlsZXNfbGltaXQgICAgICAgICAgICAgICAgPSAyMDI0MAppbm5vZGJfb3Blbl9maWxlcyAgICAgICAgICAgICAgID0gMjAyNDAKbWF4X2Nvbm5lY3RfZXJyb3JzICAgICAgICAgICAgICA9IDMwNzIKdGFibGVfb3Blbl9jYWNoZSAgICAgICAgICAgICAgICA9IDQwOTYKdGFibGVfZGVmaW5pdGlvbl9jYWNoZSAgICAgICAgICA9IDQwOTYKdG1wX3RhYmxlX3NpemUgICAgICAgICAgICAgICAgICA9IDFHCm1heF9oZWFwX3RhYmxlX3NpemUgICAgICAgICAgICAgPSAxRwoKbWF4X3N0YXRlbWVudF90aW1lID0gMTAwCgppbm5vZGJfYnVmZmVyX3Bvb2xfc2l6ZSAgICAgICAgID0gMTJHCmlubm9kYl9yZWFkX2lvX3RocmVhZHMgICAgICAgICAgPSA2NAppbm5vZGJfd3JpdGVfaW9fdGhyZWFkcyAgICAgICAgID0gNjQKaW5ub2RiX3RocmVhZF9jb25jdXJyZW5jeSAgICAgICA9IDAKaW5ub2RiX2ZsdXNoX2xvZ19hdF90cnhfY29tbWl0ICA9IDAKaW5ub2RiX2ZsdXNoX21ldGhvZCAgICAgICAgICAgICA9IE9fRElSRUNUCnBlcmZvcm1hbmNlX3NjaGVtYSAgICAgICAgICAgICAgPSAwCmlubm9kYi1maWxlLXBlci10YWJsZSAgICAgICAgICAgPSAxCmlubm9kYl9pb19jYXBhY2l0eSAgICAgICAgICAgICAgPSAyMDAwMAppbm5vZGJfdGFibGVfbG9ja3MgICAgICAgICAgICAgID0gMAppbm5vZGJfbG9ja193YWl0X3RpbWVvdXQgICAgICAgID0gMAoKc3FsX21vZGUgICAgICAgICAgICAgICAgICAgICAgICA9ICJOT19FTkdJTkVfU1VCU1RJVFVUSU9OIgoKW21hcmlhZGJdCgp0aHJlYWRfY2FjaGVfc2l6ZSAgICAgICAgICAgICAgID0gODE5Mgp0aHJlYWRfaGFuZGxpbmcgICAgICAgICAgICAgICAgID0gcG9vbC1vZi10aHJlYWRzCnRocmVhZF9wb29sX3NpemUgICAgICAgICAgICAgICAgPSAxMgp0aHJlYWRfcG9vbF9pZGxlX3RpbWVvdXQgICAgICAgID0gMjAKdGhyZWFkX3Bvb2xfbWF4X3RocmVhZHMgICAgICAgICA9IDEwMjQKCltteXNxbGR1bXBdCnF1aWNrCnF1b3RlLW5hbWVzCm1heF9hbGxvd2VkX3BhY2tldCAgICAgICAgICAgICAgPSAxMjhNCmNvbXBsZXRlLWluc2VydAoKW215c3FsXQoKW2lzYW1jaGtdCmtleV9idWZmZXJfc2l6ZSAgICAgICAgICAgICAgICAgPSAxNk0K==".decode("base64")
rSysctlFile = "bmV0LmlwdjQudGNwX2Nvbmdlc3Rpb25fY29udHJvbCA9IGJicgpuZXQuY29yZS5kZWZhdWx0X3FkaXNjID0gZnEKbmV0LmlwdjQudGNwX3JtZW0gPSA4MTkyIDg3MzgwIDEzNDIxNzcyOApuZXQuaXB2NC51ZHBfcm1lbV9taW4gPSAxNjM4NApuZXQuY29yZS5ybWVtX2RlZmF1bHQgPSAyNjIxNDQKbmV0LmNvcmUucm1lbV9tYXggPSAyNjg0MzU0NTYKbmV0LmlwdjQudGNwX3dtZW0gPSA4MTkyIDY1NTM2IDEzNDIxNzcyOApuZXQuaXB2NC51ZHBfd21lbV9taW4gPSAxNjM4NApuZXQuY29yZS53bWVtX2RlZmF1bHQgPSAyNjIxNDQKbmV0LmNvcmUud21lbV9tYXggPSAyNjg0MzU0NTYKbmV0LmNvcmUuc29tYXhjb25uID0gMTAwMDAwMApuZXQuY29yZS5uZXRkZXZfbWF4X2JhY2tsb2cgPSAyNTAwMDAKbmV0LmNvcmUub3B0bWVtX21heCA9IDY1NTM1Cm5ldC5pcHY0LnRjcF9tYXhfdHdfYnVja2V0cyA9IDE0NDAwMDAKbmV0LmlwdjQudGNwX21heF9vcnBoYW5zID0gMTYzODQKbmV0LmlwdjQuaXBfbG9jYWxfcG9ydF9yYW5nZSA9IDIwMDAgNjUwMDAKbmV0LmlwdjQudGNwX25vX21ldHJpY3Nfc2F2ZSA9IDEKbmV0LmlwdjQudGNwX3Nsb3dfc3RhcnRfYWZ0ZXJfaWRsZSA9IDAKbmV0LmlwdjQudGNwX2Zpbl90aW1lb3V0ID0gMTUKbmV0LmlwdjQudGNwX2tlZXBhbGl2ZV90aW1lID0gMzAwCm5ldC5pcHY0LnRjcF9rZWVwYWxpdmVfcHJvYmVzID0gNQpuZXQuaXB2NC50Y3Bfa2VlcGFsaXZlX2ludHZsID0gMTUKZnMuZmlsZS1tYXg9MjA5NzA4MDAKZnMubnJfb3Blbj0yMDk3MDgwMApmcy5haW8tbWF4LW5yPTIwOTcwODAwCm5ldC5pcHY0LnRjcF90aW1lc3RhbXBzID0gMQpuZXQuaXB2NC50Y3Bfd2luZG93X3NjYWxpbmcgPSAxCm5ldC5pcHY0LnRjcF9tdHVfcHJvYmluZyA9IDEKbmV0LmlwdjQucm91dGUuZmx1c2ggPSAxCm5ldC5pcHY2LnJvdXRlLmZsdXNoID0gMQ==".decode("base64")
rXCserviceFile = "IyEvYmluL2Jhc2gKClNDUklQVD0vaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2RlcwpVU0VSPSQod2hvYW1pKQoKaWYgW1sgJFVTRVIgIT0gInJvb3QiIF1dOyB0aGVuCiAgZWNobyAiUGxlYXNlIHJ1biBhcyByb290ISIKICBleGl0IDAKZmkKCnN0YXJ0KCkgewogIHBpZHM9JChwZ3JlcCAtdSB4dHJlYW1jb2RlcyBuZ2lueCB8IHdjIC1sKQogIGlmIFsgJHBpZHMgIT0gMCBdOyB0aGVuCiAgICBlY2hvICd4dHJlYW1jb2RlcyBpcyBhbHJlYWR5IHJ1bm5pbmcnCiAgICByZXR1cm4gMQogIGZpCiAgZWNobyAnU3RhcnRpbmcgeHRyZWFtY29kZXMuLi4nCgogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMgoKICBzdWRvIC11IHh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9iaW4vcGhwIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL2Nyb25zL3NldHVwX2NhY2hlLnBocAogIHN1ZG8gLXUgeHRyZWFtY29kZXMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2Jpbi9waHAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvdG9vbHMvc2lnbmFsX3JlY2VpdmVyLnBocCA+L2Rldi9udWxsIDI+L2Rldi9udWxsICYKICBzdWRvIC11IHh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9iaW4vcGhwIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3Rvb2xzL3BpcGVfcmVhZGVyLnBocCA+L2Rldi9udWxsIDI+L2Rldi9udWxsICYKICBjaG93biAtUiB4dHJlYW1jb2Rlczp4dHJlYW1jb2RlcyAvc3lzL2NsYXNzL25ldAogIGNob3duIC1SIHh0cmVhbWNvZGVzOnh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzID4vZGV2L251bGwgMj4vZGV2L251bGwKICBzbGVlcCAxCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMS5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMS5jb25mCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMi5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMi5jb25mCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMy5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMy5jb25mCiAgc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvNC5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvNC5jb25mCiAgc2xlZXAgMwogIGNobW9kICt4IC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54X3J0bXAvc2Jpbi9uZ2lueF9ydG1wCiAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbnhfcnRtcC9zYmluL25naW54X3J0bXAKICBzbGVlcCAxCiAgY2htb2QgK3ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbngvc2Jpbi9uZ2lueAogIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54L3NiaW4vbmdpbngKICBlY2hvICdSdW5uaW5nIGluIGZvcmVncm91bmQuLi4nCiAgc2xlZXAgaW5maW5pdHkKfQoKc3RvcCgpIHsKICBwaWRzPSQocGdyZXAgLXUgeHRyZWFtY29kZXMgbmdpbnggfCB3YyAtbCkKICBpZiBbWyAkcGlkcyA9IDAgXV07IHRoZW4KICAgIGVjaG8gJ3h0cmVhbWNvZGVzIGlzIG5vdCBydW5uaW5nJwogICAgcmV0dXJuIDEKICBmaQogIGVjaG8gJ1N0b3BwaW5nIHh0cmVhbWNvZGVzLi4uJwogIHN1ZG8ga2lsbGFsbCAtdSB4dHJlYW1jb2RlcwogIHNsZWVwIDEKICBzdWRvIGtpbGxhbGwgLXUgeHRyZWFtY29kZXMKICBzbGVlcCAxCiAgc3VkbyBraWxsYWxsIC11IHh0cmVhbWNvZGVzCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMQogIGtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICcvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlJyB8IGF3ayAne3ByaW50ICQyfScpIDI+L2Rldi9udWxsCiAgc2xlZXAgMgoKfQoKcmVzdGFydCgpIHsKICBzdG9wCiAgI3BzIC1VIHh0cmVhbWNvZGVzIHwgZWdyZXAgLXYgImZmbXBlZ3xQSUQiIHwgYXdrICd7cHJpbnQgJDF9JyB8IHhhcmdzIGtpbGwgLTkKICBzdGFydAp9CgpyZWxvYWQoKSB7CiAgcGlkcz0kKHBncmVwIC11IHh0cmVhbWNvZGVzIG5naW54IHwgd2MgLWwpCiAgaWYgW1sgJHBpZHMgPSAwIF1dOyB0aGVuCiAgICBlY2hvICd4dHJlYW1jb2RlcyBuZ2lueCBpcyBub3QgcnVubmluZycKICAgIHJldHVybiAxCiAgZmkKICBlY2hvICdSZWxvYWRpbmcgbmdpbnggY29uZmlnIGZvciB4dHJlYW1jb2Rlcy4uLicKICAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9uZ2lueC9zYmluL25naW54IC1zIHJlbG9hZAogIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL25naW54X3J0bXAvc2Jpbi9uZ2lueF9ydG1wIC1zIHJlbG9hZAp9CgpjYXNlICIkMSIgaW4KICBzdGFydCkKICAgIHN0YXJ0CiAgICA7OwogIHN0b3ApCiAgICBzdG9wCiAgICA7OwogIHJlbG9hZCkKICAgIHJlbG9hZAogICAgOzsKICByZXN0YXJ0KQogICAgcmVzdGFydAogICAgOzsKICAqKQogICAgZWNobyAiVXNhZ2U6ICQwIHtzdGFydHxzdG9wfHJlc3RhcnR8cmVsb2FkfSIKZXNhYwoKZXhpdCAw==".decode("base64")
rNewStartServices = "IyEgL2Jpbi9iYXNoCmtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICdzdGFydF9zZXJ2aWNlcy5zaCcgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbApzbGVlcCAxCmtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICdzdGFydF9zZXJ2aWNlcy5zaCcgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbApzbGVlcCAxCmtpbGwgJChwcyBhdXggfCBncmVwICd4dHJlYW1jb2RlcycgfCBncmVwIC12IGdyZXAgfCBncmVwIC12ICdzdGFydF9zZXJ2aWNlcy5zaCcgfCBhd2sgJ3twcmludCAkMn0nKSAyPi9kZXYvbnVsbApzbGVlcCA0CnN1ZG8gLXUgeHRyZWFtY29kZXMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2Jpbi9waHAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvY3JvbnMvc2V0dXBfY2FjaGUucGhwCnN1ZG8gLXUgeHRyZWFtY29kZXMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2Jpbi9waHAgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvdG9vbHMvc2lnbmFsX3JlY2VpdmVyLnBocCA+L2Rldi9udWxsIDI+L2Rldi9udWxsICYKc3VkbyAtdSB4dHJlYW1jb2RlcyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvYmluL3BocCAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy90b29scy9waXBlX3JlYWRlci5waHAgPi9kZXYvbnVsbCAyPi9kZXYvbnVsbCAmCmNob3duIC1SIHh0cmVhbWNvZGVzOnh0cmVhbWNvZGVzIC9zeXMvY2xhc3MvbmV0CmNob3duIC1SIHh0cmVhbWNvZGVzOnh0cmVhbWNvZGVzIC9ob21lL3h0cmVhbWNvZGVzICA+L2Rldi9udWxsIDI+L2Rldi9udWxsCnNsZWVwIDQKY2htb2QgK3ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbnhfcnRtcC9zYmluL25naW54X3J0bXAKY2htb2QgK3ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvL25naW54L3NiaW4vbmdpbngKL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbnhfcnRtcC9zYmluL25naW54X3J0bXAKL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvbmdpbngvc2Jpbi9uZ2lueApzdGFydC1zdG9wLWRhZW1vbiAtLXN0YXJ0IC0tcXVpZXQgLS1waWRmaWxlIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC8xLnBpZCAtLWV4ZWMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL3NiaW4vcGhwLWZwbSAtLSAtLWRhZW1vbml6ZSAtLWZwbS1jb25maWcgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2V0Yy8xLmNvbmYKc3RhcnQtc3RvcC1kYWVtb24gLS1zdGFydCAtLXF1aWV0IC0tcGlkZmlsZSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMi5waWQgLS1leGVjIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9zYmluL3BocC1mcG0gLS0gLS1kYWVtb25pemUgLS1mcG0tY29uZmlnIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC9ldGMvMi5jb25mCnN0YXJ0LXN0b3AtZGFlbW9uIC0tc3RhcnQgLS1xdWlldCAtLXBpZGZpbGUgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzMucGlkIC0tZXhlYyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvc2Jpbi9waHAtZnBtIC0tIC0tZGFlbW9uaXplIC0tZnBtLWNvbmZpZyAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvZXRjLzMuY29uZgpzdGFydC1zdG9wLWRhZW1vbiAtLXN0YXJ0IC0tcXVpZXQgLS1waWRmaWxlIC9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC80LnBpZCAtLWV4ZWMgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL3NiaW4vcGhwLWZwbSAtLSAtLWRhZW1vbml6ZSAtLWZwbS1jb25maWcgL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwL2V0Yy80LmNvbmYKIA==".decode("base64")
rSystemdUnitFile = "=W1VuaXRdClNvdXJjZVBhdGg9L2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZQpEZXNjcmlwdGlvbj14dHJlYW1jb2RlcyBzZXJ2aWNlCkFmdGVyPW5ldHdvcmsudGFyZ2V0ClN0YXJ0TGltaXRJbnRlcnZhbFNlYz0wCiAKW1NlcnZpY2VdClR5cGU9c2ltcGxlClVzZXI9cm9vdApSZXN0YXJ0PW9uLWZhaWx1cmUKUmVzdGFydFNlYz01CkV4ZWNTdGFydD0vYmluL2Jhc2ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZSBzdGFydApFeGVjUmVzdGFydD0vYmluL2Jhc2ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZSByZXN0YXJ0CkV4ZWNTdG9wPS9iaW4vYmFzaCAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9zZXJ2aWNlIHN0b3AKRXhlY1JlbG9hZD0vYmluL2Jhc2ggL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvc2VydmljZSByZWxvYWQKIApbSW5zdGFsbF0KV2FudGVkQnk9bXVsdGktdXNlci50YXJnZXQ==".decode("base64")
rNginxBalanceFile = "dXBzdHJlYW0gcGhwIHsKICAgIGxlYXN0X2Nvbm47CiAgICBzZXJ2ZXIgdW5peDovaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMS5zb2NrOwogICAgc2VydmVyIHVuaXg6L2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzIuc29jazsKICAgIHNlcnZlciB1bml4Oi9ob21lL3h0cmVhbWNvZGVzL2lwdHZfeHRyZWFtX2NvZGVzL3BocC8zLnNvY2s7CiAgICBzZXJ2ZXIgdW5peDovaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvNC5zb2NrOwp9Cg==".decode("base64")
rPhpfpm1 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzEucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMS5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")
rPhpfpm2 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzIucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMi5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")
rPhpfpm3 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzMucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvMy5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")
rPhpfpm4 = "W2dsb2JhbF0KcGlkID0gL2hvbWUveHRyZWFtY29kZXMvaXB0dl94dHJlYW1fY29kZXMvcGhwLzQucGlkCmV2ZW50cy5tZWNoYW5pc20gPSBlcG9sbApkYWVtb25pemUgPSB5ZXMKcmxpbWl0X2ZpbGVzID0gMTAwMDAKW3h0cmVhbWNvZGVzXQp1c2VyID0geHRyZWFtY29kZXMKZ3JvdXAgPSB4dHJlYW1jb2RlcwpsaXN0ZW4gPSAvaG9tZS94dHJlYW1jb2Rlcy9pcHR2X3h0cmVhbV9jb2Rlcy9waHAvNC5zb2NrCmxpc3Rlbi5hbGxvd2VkX2NsaWVudHMgPSAxMjcuMC4wLjEKbGlzdGVuLm93bmVyID0geHRyZWFtY29kZXMKbGlzdGVuLmdyb3VwID0geHRyZWFtY29kZXMKbGlzdGVuLm1vZGUgPSAwNjYwCnBtID0gZHluYW1pYwpwbS5tYXhfY2hpbGRyZW4gPSA0MDAKcG0uc3RhcnRfc2VydmVycyA9IDMyCnBtLm1pbl9zcGFyZV9zZXJ2ZXJzID0gMTYKcG0ubWF4X3NwYXJlX3NlcnZlcnMgPSAzMgpwbS5wcm9jZXNzX2lkbGVfdGltZW91dCA9IDNzCnNlY3VyaXR5LmxpbWl0X2V4dGVuc2lvbnMgPSAucGhwCg==".decode("base64")
rlibjemalloc = "W1NlcnZpY2VdCkxpbWl0Tk9GSUxFPTY1NTM1MApFbnZpcm9ubWVudD0iTERfUFJFTE9BRD0vdXNyL2xpYi94ODZfNjQtbGludXgtZ251L2xpYmplbWFsbG9jLnNvLjEiCg==".decode("base64")
# i am lazy to prepare normal versions with escaped characters, use base64 decode/encode to read or change these.

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
    os.system("apt-get upgrade -y > /dev/null")
    printc("Removing libcurl4 if installed")
    os.system("apt-get remove --auto-remove libcurl4 -y > /dev/null")
    printc("Installing Curl with Snap")
    os.system("sudo apt -y install snapd && snap install curl > /dev/null")
    if rType == "MAIN":
        printc("Adding Mariadb Repository")
        if rVersion in rVersions:
            #os.system("sudo apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'")
            #https://mariadb.com/kb/en/installing-mariadb-deb-files/
            os.system("sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8")
            os.system("sudo add-apt-repository -y 'deb [arch=amd64,arm64,ppc64el] http://ams2.mirrors.digitalocean.com/mariadb/repo/10.5/ubuntu %s main'" % rVersions[rVersion])
            os.system("apt-get update > /dev/null")
    for rPackage in rPackages:
        printc("Installing %s" % rPackage)
        os.system("apt-get install %s -y > /dev/null" % rPackage)
    printc("Installing libpng")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb")
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
    os.system('wget --user-agent="Mozilla/5.0" -q -O "/tmp/xtreamcodes.tar.gz" "%s"' % rURL)
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
    rURL = "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/release_22f.zip"
    printc("Downloading Admin Panel")  
    os.system('wget --user-agent="Mozilla/5.0"  -q -O "/tmp/update.zip" "%s"' % rURL)
    if os.path.exists("/tmp/update.zip"):
        try: is_ok = zipfile.ZipFile("/tmp/update.zip")
        except:
            printc("Invalid link or zip file is corrupted for /tmp/update.zip!", col.FAIL)
            os.remove("/tmp/update.zip")
            return False
    printc("Installing Admin Panel")
    os.system('unzip -o /tmp/update.zip -d /tmp/update/ > /dev/null && cp -rf /tmp/update/XtreamUI-master/* /home/xtreamcodes/iptv_xtream_codes/ > /dev/null && rm -rf /tmp/update/XtreamUI-master > /dev/null && rm -rf /tmp/update > /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes > /dev/null')
    try: os.remove("/tmp/update.zip")
    except: pass
    rURL2 = "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/newstuff.zip"
    printc("Downloading New Stuff for Admin Panel")  
    os.system('wget --user-agent="Mozilla/5.0"  -q -O "/tmp/update2.zip" "%s"' % rURL2)
    if os.path.exists("/tmp/update2.zip"):
        try: is_ok = zipfile.ZipFile("/tmp/update2.zip")
        except:
            printc("Invalid link or zip file is corrupted for /tmp/update2.zip!", col.FAIL)
            os.remove("/tmp/update2.zip")
            return False
        printc("Installing New Stuff for Admin Panel")
        os.system('unzip -o /tmp/update2.zip -d /tmp/update2/ > /dev/null && cp -rf /tmp/update2/* /home/xtreamcodes/iptv_xtream_codes/ > /dev/null && rm -rf /tmp/update2/* > /dev/null && rm -rf /tmp/update2 > /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/ > /dev/null > /dev/null')
        if os.path.exists("/tmp/xtreamui-things"): os.system("rm -rf /tmp/xtreamui-things")
        try: os.remove("/tmp/update2.zip")
        except: pass

        printc("Getting updated admin-modified files")
        os.system('wget --user-agent="Mozilla/5.0"  -q -O "/tmp/xtreamuithings.zip" "https://github.com/emre1393/xtreamui-things/archive/refs/heads/master.zip"')
        try: is_ok = zipfile.ZipFile("/tmp/xtreamuithings.zip")
        except:
            printc("Invalid link or zip file is corrupted for /tmp/xtreamuithings.zip!", col.FAIL)
            os.remove("/tmp/xtreamuithings.zip")
            return False
        os.system('unzip -o /tmp/xtreamuithings.zip -d /tmp/ > /dev/null && cp -rf /tmp/xtreamui-things-master/admin-modified/* /home/xtreamcodes/iptv_xtream_codes/admin/ > /dev/null && rm -rf /tmp/xtreamui-things-master/* > /dev/null && rm -rf /tmp/xtreamui-things-master > /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/ > /dev/null > /dev/null')
        try: os.remove("/tmp/xtreamuithings.zip")
        except: pass
        return True
    printc("Failed to download installation file!", col.FAIL)
    return False



def mysql(rUsername, rPassword):
    global rMySQLCnf
    printc("Configuring Mariadb-Server")
    rCreate = True
    if os.path.exists("/etc/mysql/my.cnf"):
        if open("/etc/mysql/my.cnf", "r").read(14) == "# Xtream Codes": rCreate = False
    if rCreate:
        shutil.copy("/etc/mysql/my.cnf", "/etc/mysql/my.cnf.xc")
        rFile = open("/etc/mysql/my.cnf", "w")
        rFile.write(rMySQLCnf)
        rFile.close()
        rFile = open("/etc/systemd/system/mariadb.service.d/libjemalloc.conf", "w")
        rFile.write(rlibjemalloc)
        rFile.close()
        os.system("systemctl daemon-reload > /dev/null")    
        os.system("systemctl restart mariadb.service > /dev/null")

    rExtra = ""
    rRet = os.system("mysql -u root -e \"SELECT VERSION();\"")
    if rRet != 0:
        while True:
            rExtra = " -p%s" %  input("Enter MySQL Root Password: ")
            rRet = os.system("mysql -u root%s -e \"SELECT VERSION();\"" % rExtra)
            if rRet == 0: break
            else: printc("Invalid password! Please try again.") 
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
            os.system('mysql -u root%s -e "CREATE USER \'%s\'@\'localhost\' IDENTIFIED BY \'%s\'; GRANT ALL PRIVILEGES ON xtream_iptvpro.* TO \'%s\'@\'localhost\' WITH GRANT OPTION; GRANT SELECT, PROCESS, LOCK TABLES ON *.* TO \'%s\'@\'localhost\';FLUSH PRIVILEGES;" > /dev/null' % (rExtra, rUsername, rPassword, rUsername, rUsername))
            os.system('mysql -u root%s -e "CREATE USER \'%s\'@\'127.0.0.1\' IDENTIFIED BY \'%s\'; GRANT ALL PRIVILEGES ON xtream_iptvpro.* TO \'%s\'@\'127.0.0.1\' WITH GRANT OPTION; GRANT SELECT, PROCESS, LOCK TABLES ON *.* TO \'%s\'@\'127.0.0.1\';FLUSH PRIVILEGES;" > /dev/null' % (rExtra, rUsername, rPassword, rUsername, rUsername))
            os.system('mysql -u root%s -e "GRANT SELECT, INSERT, UPDATE, DELETE ON xtream_iptvpro.* TO \'%s\'@\'%%\' IDENTIFIED BY \'%s\';FLUSH PRIVILEGES;" > /dev/null' % (rExtra, rUsername, rPassword))
            os.system('mysql -u root%s -e "USE xtream_iptvpro; CREATE TABLE IF NOT EXISTS dashboard_statistics (id int(11) NOT NULL AUTO_INCREMENT, type varchar(16) NOT NULL DEFAULT \'\', time int(16) NOT NULL DEFAULT \'0\', count int(16) NOT NULL DEFAULT \'0\', PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=latin1; INSERT INTO dashboard_statistics (type, time, count) VALUES(\'conns\', UNIX_TIMESTAMP(), 0),(\'users\', UNIX_TIMESTAMP(), 0);\" > /dev/null' % rExtra)
            #last one is to prevent an xc vulnerability, run "UPDATE settings SET get_real_ip_client='HTTP_CF_CONNECTING_IP' where id=1;" query if you are using cf proxy.
            os.system('mysql -u root%s -e "USE xtream_iptvpro; UPDATE settings SET get_real_ip_client=\'\', double_auth=\'1\', hash_lb=\'1\', mag_security=\'1\' where id=\'1\';" > /dev/null'  % rExtra)

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
    os.system("mount -a")
    try: os.remove("/usr/bin/ffmpeg")
    except: pass
    if not os.path.exists("/home/xtreamcodes/iptv_xtream_codes/tv_archive"): os.mkdir("/home/xtreamcodes/iptv_xtream_codes/tv_archive/")
    os.system("ln -s /home/xtreamcodes/iptv_xtream_codes/bin/ffmpeg /usr/bin/")
    os.system("chmod -R 0777 /home/xtreamcodes > /dev/null")
    if rType == "MAIN": 
        os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/admin/ -type f -exec chmod 644 {} \;")
        os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/admin/ -type d -exec chmod 755 {} \;")
        os.system("sed -i 's|https://raw.githubusercontent.com/emre1393/xtreamui_mirror/refs/heads/master/balancer.py|https://github.com/emre1393/xtreamui_mirror/raw/master/withmariadb/balancer.py|g'  /home/xtreamcodes/iptv_xtream_codes/pytools/balancer.py")
    #adds domain/user/pass/id.ts url support
    with open('/home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf', 'r') as nginx_file:
        nginx_replace = nginx_file.read()
        nginx_replace = nginx_replace.replace("rewrite ^/(.*)/(.*)/(\\d+)$ /streaming/clients_live.php?username=$1&password=$2&stream=$3&extension=ts break;", "rewrite ^/(.*)/(.*)/(\\d+)\\.(.*)$ /streaming/clients_live.php?username=$1&password=$2&stream=$3&extension=$4 break;\r\n        rewrite ^/(.*)/(.*)/(\\d+)$ /streaming/clients_live.php?username=$1&password=$2&stream=$3&extension=ts break;\r\n")
    with open('/home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf', 'w') as nginx_file:
        nginx_file.write(nginx_replace)
    os.system("wget --user-agent=\"Mozilla/5.0\"  -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/nginx -O /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/nginx_rtmp -O /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/sbin/nginx_rtmp")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/pid_monitor.php -O /home/xtreamcodes/iptv_xtream_codes/crons/pid_monitor.php")
    os.system("sudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx/sbin/nginx")
    os.system("sudo chmod +x /home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/sbin/nginx_rtmp")
    os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/wwwdir/ -type f -exec chmod 644 {} \;")
    os.system("sudo find /home/xtreamcodes/iptv_xtream_codes/wwwdir/ -type d -exec chmod 755 {} \;")
    os.system("chmod 0700 /home/xtreamcodes/iptv_xtream_codes/config > /dev/null")
    os.system("sed -i 's|echo \"Xtream Codes Reborn\";|header(\"Location: https://www.google.com/\");|g' /home/xtreamcodes/iptv_xtream_codes/wwwdir/index.php")
    os.system("wget --user-agent=\"Mozilla/5.0\" -q https://github.com/emre1393/xtreamui_mirror/releases/latest/download/GeoLite2.mmdb -O /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb")
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


def start(first=True):
    if first: printc("Starting Xtream Codes")
    else: printc("Restarting Xtream Codes")
    os.system("sudo systemctl start xtreamcodes")


if __name__ == "__main__":

    try: rVersion = os.popen('lsb_release -sr').read().strip()
    except: rVersion = None
    if not rVersion in rVersions:
        printc("Unsupported Operating System, Works only on Ubuntu Server 16 and 18")
        sys.exit(1)

    printc("Xtream UI - Installer Mirror", col.OKGREEN, 2)
    print "%s │ Check out the mirror repo: https://github.com/emre1393/xtreamui_mirror/withmariadb %s" % (col.OKGREEN, col.ENDC)
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
