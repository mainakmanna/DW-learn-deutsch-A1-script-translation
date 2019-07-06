import urllib3
from bs4 import BeautifulSoup
import os
http = urllib3.PoolManager()
URL_CONTAINER_FILE = 'url_list_file'
with open(URL_CONTAINER_FILE, 'rb') as f:
    contents = f.read()
#contents = contents.decode("ISO-8859-1")
contents = contents.decode("utf-8")
# you may also want to remove whitespace characters like `\n` at the end of each line
contents = contents.split('\n')
#print(contents)
#contents.sort()
OUTPUT = r"./output"
if os.path.exists(OUTPUT) and os.path.isdir(OUTPUT):
    print('INFO: DIrectory Exists')
else:
    os.mkdir(OUTPUT)
    
os.chdir(OUTPUT)

index = 1
for url in contents:
    if len(url) > 0 :
        url = url.replace('\r','')
        print(url)
        response = http.request('GET', url+'/lm')
        soup = BeautifulSoup(response.data, features="html.parser")
        p = soup.find_all("div",class_="richtext-content-container")
        s = p[0].get_text()
        #print(s)
        s = s.splitlines()
        #print(url.split('/'))
        filename = url.split('/')[-2]+'.md'
        with open(str(index)+'-'+filename,'w', encoding="utf-8")as text_file:
            #text_file.write('|DE|EN|\n')
            #text_file.write('|---|---|\n')
            
            for line in s:
                if len(line) > 0 :
                    #text_file.write('|'+line+'||\n')
                    text_file.write((line+'\n'))
            text_file.close()
        #break
    index = index + 1
