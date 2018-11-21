
# coding: utf-8

# In[30]:

import telnetlib
import sys
import time

host='ptt.cc'


userlist = [['user1','password1'],['user2','password2']]

def login(host,user,password):
    print(host +'\n' + user +'\n' + password + '\r\n')
    global telnet
    telnet = telnetlib.Telnet(host)
    time.sleep(1)
    content = telnet.read_very_eager().decode('big5','ignore')
    #print(content)
    
    if u'系統過載' in content:
        print('系統過載中')
        sys.exit()
    
    if u'請輸入代號' in content:
        print ('Entering account..')
        telnet.write(user.encode('ascii') + b'\r\n')
        #Write a byte string to the socket  ^ 換成byte
        time.sleep(1)
        
        content = telnet.read_very_eager().decode('big5','ignore')
        #print (content)
        
        
        if u'請輸入您的密碼' in content:
            print ('Entering password..')
            telnet.write(password.encode('ascii') + b'\r\n')
            time.sleep(1)
            
            content = telnet.read_very_eager().decode('big5','ignore')
            print (content)
        
            telnet.write(b'\r\n')
            print('login success1')
        
        if u'您想刪除其他重複登入的連線嗎？' in content:
            
            print('Logout others')
            telnet.write(b'n\r\n')
            time.sleep(1)
            telnet.write(b'\r\n')
            print('')
            content = telnet.read_very_eager().decode('big5','ignore')
            #print (content)
            print('login success')

def logout():
    
    print("logout...")
    # q = 上一頁 g = 離開 y = 確認
    telnet.write(b'qqqqqqqqqg\r\ny\r\n')
    time.sleep(1)
    telnet.close()
    print('logout success')
        
def main():
    for i in range (len(userlist)) :
        userdata=userlist[i]
        login(host,userdata[0],userdata[1])
        time.sleep(3)
        logout()


if __name__ == '__main__' :
    main()


    

    


# In[ ]:



