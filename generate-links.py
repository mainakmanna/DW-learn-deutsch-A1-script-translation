"""
This program generates the links for the A1 course. These links point to
the script pages.
"""

import urllib3
from bs4 import BeautifulSoup

COURSE_LINK = "https://learngerman.dw.com/en/beginners/c-36519789"
http = urllib3.PoolManager()
response = http.request('GET', COURSE_LINK)

count = 0
BASE_URL = 'https://learngerman.dw.com'
URL_CONTAINER_FILE = 'url_list_file'
with open(URL_CONTAINER_FILE, "w", encoding="utf-8") as text_file:    
    # getting all the <a> elements from the HTML page.
    for link in BeautifulSoup(response.data,  features="html.parser").find_all('a'):
        if link.has_attr('href'):
            urlpart = link['href']
            # Consider only the links which contain the transcripts. Ends with "l-" 
            # https://learngerman.dw.com/en/hallo/l-37250531/lm For example.
            if urlpart.split('/')[-1][0:2] == "l-":
                count = count + 1
                print(BASE_URL+urlpart)
                text_file.write(BASE_URL+urlpart+'\n')
    print(count)