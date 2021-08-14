# README #
# xtreamui_mirror

This is an installation mirror for xtream ui software.

### How do I install? ###

update your ubuntu first, then install panel  
  
* sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install libxslt1-dev libcurl3 libgeoip-dev python -y;  
* wget https://github.com/emre1393/xtreamui_mirror/raw/master/install.py; 
* sudo python install.py  
  
If you want to install main server with admin panel, choose MAIN.  
If you want to install load balance on additional servers, add a server to panel in manage servers page, then run script and proceed with LB option.  

### tutorials are here; ###

[Xtream-UI Tutorials](https://www.youtube.com/playlist?list=PLJB51brdC_w7dTDxi1MPqiuk3JH5U2ekn "Xtream-UI Tutorials")


### Files Hashes ###
* main_xtreamcodes_reborn.tar
* sha1: "532B63EA0FEA4E6433FC47C3B8E65D8A90D5A4E9"

* sub_xtreamcodes_reborn.tar
* sha1: "5F8A7643A9E7692108E8B40D0297A7A5E4423870"

* release_22f.zip
* sha-1: "95471A7EFEB49D7A1F52BAB683EA2BF849F79983"

* newstuff.zip  
* sha-1: "AE46E6FE4C19791BF1EE6869D11D51888476ACAB"  

note: newstuff.zip has same files from my xtreamui_things repo, i won't update this zip file anymore. if i change something on those files, you can download them.  
note2: also i still use same release_22f.zip file. if you want to use old install.py, go to bitbucket mirror page.

### note,
i forked this install.py is from https://xtream-ui.com/install/install.py  
you can compare my install.py with original one.
