# Xtream UI for Ubuntu 20.04 install
This is an installation mirror for xtream ui software on Ubuntu 20.04.
Includes NGINX 1.19.2 and PHP 7.3.25.

### Update 08/12/2020: ###
- bumped php version from 7.2 to 7.3 following 7.2 obsolence
- fixed user_watcher.php disconnect users every minute because of wrong pid check.

### THANKS ###

Thanks to GTA for xtream-ui admin original interface
Thanks to emre1393 for being the wisdom of xui community

### Installation: ###

Update your ubuntu first, then install panel:
``` 
sudo apt update && sudo apt full-upgrade -y && sudo apt install curl python2 -y;  
wget https://github.com/NeySlim/xtreamui_mirror/raw/master/install.py; 
sudo python2 install.py  
```
  
If you want a whole NEW installation, choose MAIN and then UPDATE.  
If you want to install load balance on additional servers, add a server to panel in manage servers page, then run script and proceed with LB option.  
If you want to update admin panel, select UPDATE.

### tutorials are here; ###

[Xtream-UI Tutorials](https://www.youtube.com/playlist?list=PLJB51brdC_w7dTDxi1MPqiuk3JH5U2ekn "Xtream-UI Tutorials")


### notes from emre1393:

I forked this install.py is from https://xtream-ui.com/install/install.py  
btw, developer removed admin part from original install.py at begining of this year.  
you can compare my install.py with original one.

Developer made update releases open to public after r22c release, you can download them from https://xtream-ui.com.  
i added an "UPDATE" part to install.py, it will ask link of update zip file.
