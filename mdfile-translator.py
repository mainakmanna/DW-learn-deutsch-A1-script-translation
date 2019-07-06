import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


DIR_PATH = r'./output'



# if directory exists
if os.path.exists(DIR_PATH) and os.path.isdir(DIR_PATH):
    print('[Info]: Directory mentioned in DIR_NAME exists. ')
    #os.chdir(DIR_PATH)
    # Iterating over all the files in directory
    for filename in os.listdir(DIR_PATH):
        browser = webdriver.Chrome()
        browser.get(('https://translate.google.co.in/'))
        print('[Info]: Working in file := ' + filename)
        _, fileExt = os.path.splitext(filename)
        # Only work in markdown files.
        if fileExt == '.md':
            translatedFile = []
            with open(DIR_PATH+'/'+filename, 'r', encoding="utf-8") as fileRead:
                lines = []
                ct = 0
                username = browser.find_element_by_id('source')

                str = ""
                for line in fileRead:
                    str = str + line
                print(str)

                originalStringLines =  str.splitlines()
                ctx  = 0
                bigy = originalStringLines
                username.send_keys(str)

                print("ok1")
                time.sleep(5)
                print("ok5")
                ff = browser.find_element_by_css_selector('span.tlid-translation.translation').text
                print(ff)
                ff = ff.splitlines()
                bigx = ff
            towrite = '|DE|EN|\n|---|---|\n'
            for i in range(len(bigx)):
                towrite = towrite + '|' + bigy[i] + '|' + bigx[i] + '|\n'

            with open(DIR_PATH+'/'+filename, 'w', encoding="utf-8") as fw:
                fw.writelines(towrite)
                fw.close()
            browser.quit()
            #webdriver.close()
            #browser.find_element_by_css_selector('div.clear.jfk-button-flat.tlid-clear-source-text.jfk-button').click()
            #break

else:
    print('[Error]: Directory mentioned in DIR_NAME doesn\'t exist.')