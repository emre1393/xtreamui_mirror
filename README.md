# README #
# xui20

This is an installation mirror for xtream ui software on Ubuntu 20.04.

Includes ginx 1.19.2 and php-fpm 7.2.33 compiled.

### THANKS ###

Thanks to GTA for xtream-ui.

Thanks to emre1393, who I stole everything (even this readme file) to make this Ubuntu 20.04 release possible.

### How do I install? ###

update your ubuntu first, then install panel  
 

``` 
sudo apt update && sudo apt full-upgrade -y && sudo apt install python2 -y;  
wget https://github.com/NeySlim/xtreamui_mirror/raw/master/install.py; 
sudo python2 install.py  
```
  
If you want a whole NEW installation, choose MAIN and then UPDATE.  
If you want to install load balance on additional servers, add a server to panel in manage servers page, then run script and proceed with LB option.  
If you want to update admin panel, select UPDATE, then paste download link of release_xyz.zip file.  

### tutorials are here; ###

[Xtream-UI Tutorials](https://www.youtube.com/playlist?list=PLJB51brdC_w7dTDxi1MPqiuk3JH5U2ekn "Xtream-UI Tutorials")


### Files sha1 Hashes ###

* 69a7a7f17a98def40f1a1c0de6e2f1d5de40e243  main_xtreamcodes_reborn.tar.gz
* 6e9b3f7cd2510d1fecb62fa2b9986f1296a373b7  sub_xtreamcodes_reborn.tar.gz

### notes from emre1393,

I forked this install.py is from https://xtream-ui.com/install/install.py  
btw, developer removed admin part from original install.py at begining of this year.  
you can compare my install.py with original one.

Developer made update releases open to public after r22c release, you can download them from https://xtream-ui.com.  
i added an "UPDATE" part to install.py, it will ask link of update zip file.
