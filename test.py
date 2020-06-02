from flask import Flask,render_template,request
app = Flask(__name__)


from selenium import webdriver

import pyperclip
import names

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime



@app.route('/',methods=["GET","POST"])
def prob():
    if request.method=="POST":
        # try:
            register()
            return render_template('index.html')
        # except:
        #     return render_template('index.html')
            
    return render_template('index.html')

# @app.route('/stop',methods=["GET","POST"])
# def stop():
#     if request.method=="POST":
#         # try:
#             exit()
#             return render_template('index.html')
#         # except:
#         #     return render_template('index.html')
            
#     return render_template('index.html')


def register():
        
    mail=['abc']
    i=1
    l=0
    while True:
        start=time.time()
        fail=0
        
        # email=input("enter email")
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        
        try:
            # driver = webdriver.Chrome(executable_path='/Users/HP/Desktop/folders/others/chromedriver/chromedriver.exe')
            # driver = webdriver.PhantomJS()
            # driver.set_window_size(300, 300)

            # email=input("enter email")
            if fail==0:
                try:
                    url_tm='https://temp-mail.org/en/'
                    driver.get(url_tm)
                    # driver.find_element_by_id("click-to-delete").click()
                    # time.sleep(1)
                    print("copying mail...")
                    xpath1='/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button'
                    time.sleep(2)
                    driver.find_element_by_xpath(xpath1).click()
                    h=pyperclip.paste()
                    print(f"old mail id {mail[0]}")
                    print(f"new mail id {h}")
                    if h in mail:
                        print("mail not copied")
                        
                        l+=1
                        fail=1
                        driver.close()
                        
                    mail.pop()
                    mail.append(h)
                except Exception as e:
                    print("copying failed")
                    
                    if fail==0:
                        l+=1
                        driver.close()
                    fail=1
                    print(e)
                    

            if fail==0:
                try:
                    url_in='https://internshala.com/i/SRC-ISP18BALA8892'

                    # if k!=0:
                    #     driver.

                    driver.get(url_in)
                    # time.sleep(3)
                    # driver.set_window_size(500, 300)
                    print("registering...")
                    
                    #driver.find_element_by_xpath('/html/body/div[1]/div[21]/div/div/div[1]/div/div/div/div/a').click()
                    inputElement = driver.find_element_by_id("email")
                    email = pyperclip.paste()
                    inputElement.send_keys(email)
                    inputElement = driver.find_element_by_id("password")
                    inputElement.send_keys('10935143')
                    name,address=names.get_full_name().split()

                    name_ele = driver.find_element_by_id("first_name")
                    name_ele.send_keys(name)
                    name2_ele = driver.find_element_by_id("last_name")
                    name2_ele.send_keys(address)
                    driver.find_element_by_xpath('//*[@id="registration-form"]/button').click()
                except Exception as e:
                    print("registraion failed")
                    if fail==0:
                        l+=1
                        driver.close()
                    fail=1
                    print(e)

            # time.sleep(2)
            if fail==0:
                try:
                    driver.get(url_tm)
                    # time.sleep(10)
                    print("loading mail...")
                    print("waiting...",end="")
                    flag=0
                    p=0
                    while flag==0:
                        try:
                            driver.find_element_by_css_selector('body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div.col-box.hidden-xs-sm > span > a').click()
                            flag=1
                        except:
                            p+=1
                            print("...",end="")
                            if p==2000:
                                
                                flag=1
                    print("\n verifying mail")
                    time.sleep(2)
                    driver.find_element_by_css_selector('body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-data-content > div.inbox-data-content-intro > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a').click()
                except Exception as e:
                    print("verification failed")
                    if fail==0:
                        l+=1
                    fail=1
                    print(e)
            #time.sleep(2)
            # fields=driver.find_element_by_css_selector('#category_selected_preferences___chosen')
            # fields.send_keys('data science')
            # fields.sendKeys(Keys.ENTER)
            # driver.find_element_by_css_selector('#both').click()
            # driver.find_element_by_css_selector('#preference_form > div.form-group.button_container > button')
            # #driver.find_element_by_id('skip_button')
            if fail==0:
                print()
                print()
                print(" registration  completed ")
                print()
                i+=1
            
                driver.close()
            
            
        except Exception as e:
            print(e)
            print()
            print()
            print('registration FAILED')
            print()
            print()
            if fail==0:
                l+=1
            # driver.close()

        end=time.time()
        print(f"time taken : {int(end-start)}")
        print(f" \nregistration  completed :  {i}")
        print(f" registration FAILED   : {l}")






if __name__ == "__main__":
    app.run(debug=True)
