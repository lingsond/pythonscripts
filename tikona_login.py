from splinter.browser import Browser
from time import sleep
 
URL = 'https://login.tikona.in/userportal/login.do?requesturi=http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204&act=null'
NAME = 'TIKONA USERNAME'
PASSWORD = 'YOUR PASSWORD'
 
def main():
    br = Browser('chrome')
    br.visit(URL)
    sleep(3)
    if br.is_text_present("Remember me", wait_time=7):
        br.fill('username', NAME)
        br.fill('password', PASSWORD)
        br.execute_script('javascript:savesettings()')
       
 
#############################################################################
 
if __name__ == "__main__":
    main()
