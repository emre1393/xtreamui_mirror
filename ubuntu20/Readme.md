

# README #
# xtreamui_mirror for ubuntu 20

test on ubuntu 20 with updated php binaries  
it may work or may not work, idk.  

what i did, i updated php binaries (php folder), installation will unzip updated php folder, rest of installation files are same files from original install.py.
you need to use python2, it is working at least.

### How do I install? ###

update your ubuntu first, then install panel  
  
* sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install python2 -y;  
* wget https://github.com/emre1393/xtreamui_mirror/raw/master/ubuntu20/install.py; 
* sudo python2 install.py  
  
If you want a whole NEW installation, choose MAIN and then UPDATE.  
If you want to install load balance on additional servers, add a server to panel in manage servers page, then run script and proceed with LB option.  
If you want to update admin panel, select UPDATE, then paste download link of release_xyz.zip file.  

### tutorials are here; ###

[Xtream-UI Tutorials](https://www.youtube.com/playlist?list=PLJB51brdC_w7dTDxi1MPqiuk3JH5U2ekn "Xtream-UI Tutorials")


### Files Hashes ###
* main_xtreamcodes_reborn.tar
* sha1: "532B63EA0FEA4E6433FC47C3B8E65D8A90D5A4E9"

* sub_xtreamcodes_reborn.tar
* sha1: "5F8A7643A9E7692108E8B40D0297A7A5E4423870"

### note,
i forked this install.py is from https://xtream-ui.com/install/install.py  
btw, developer removed admin part from original install.py at begining of this year.  
you can compare my install.py with original one.

### note2,
edit pytools/balancer.py to use "auto lb installer" from this mirror. auto lb installer added to panel with update    
`sed -i 's|"https://xtream-ui.com/install/balancer.py"|"https://github.com/emre1393/xtreamui_mirror/raw/master/ubuntu20/balancer.py"|g' /home/xtreamcodes/iptv_xtream_codes/pytools/balancer.py`  

### note3,  
developer made update releases open to public after r22c release, you can download them from https://xtream-ui.com.  
i added an "UPDATE" part to install.py, it will ask link of update zip file.  

### note4,  
updated php binaries with php 7.4.10 version, compiled according to how-to txt and also added geoip.so, mcrypt.so, mysqli.so from php pecl repository.  
mysql-server 8 is used, config file adapted (barely),  
you must create mysql user with  
CREATE USER 'auser_iptvpro'@'%' IDENTIFIED WITH mysql_native_password BY 'passwd_here'; GRANT ALL PRIVILEGES ON xtream_iptvpro.* TO 'user_iptvpro'@'%' WITH GRANT OPTION; GRANT SELECT, LOCK TABLES ON *.* TO 'user_iptvpro'@'%'; FLUSH PRIVILEGES;  