PTT auto Login tutorial
=======

## Tools

     Python3
     GCP compute engine
     
     
---
use **telnetlib** to connect
```Python=
host='ptt.cc'
userlist = [['user1','password1'],['user2','password2']]
```
> Remember to modify user name and password

## Upload to GCP compute engine

### New VM instance

![](https://i.imgur.com/lsRq52v.png)

### Connect to VM

Click SSH to connect to terminal
![](https://i.imgur.com/SDWZvZq.png)


### Upload file
![](https://i.imgur.com/HtNoQT0.png)



排程，每天執行
```
crontab -e
```
```
0 9  * * * /usr/bin/python3  /home/m10515085/pttauto_v02.py
```
> 分 時 日 月 星期 要執行的指令
> 每天早上10點透過python3執行
> 


## Reference
* https://stackoverflow.com/questions/29527469/executing-python3-file-with-a-cron-job
* https://docs.python.org/2/library/telnetlib.html
* https://www.youtube.com/watch?v=FkdR6C-a9Nw
