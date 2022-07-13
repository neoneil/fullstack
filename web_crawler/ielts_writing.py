from email import header
from bs4 import BeautifulSoup
import requests
from csv import writer
from array import *
url = "https://howtodoielts.com/recent-ielts-writing-topics-2022/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('blockquote',class_="wp-block-quote")


with open('writing_questions2.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['test', 'question1', 'question2', 'date']
    thewriter.writerow(header)
    two_d_items = []
    for list in lists:
        ps = list.find_all('p')
        #print(ps)
        rows=[]
        i = 0
        for p in ps:
            if(len(p.find_all()) == 0):
                #print(p.text)  
                rows.append(p.text)
                i = i + 1
        if(i==2):
            rows.append('NULL')
        rows.append(list.find('cite'))
        two_d_items.append(rows)
        # thewriter.writerow(rows)
    
        # print(list.find('cite').text)
        
    print(two_d_items)
    thewriter.writerows(two_d_items)




# for list in lists:
#     text = len(list.find_all('p',recursive=False))

#     info = [text]
#     print(info)



# for list in lists:
#     text = list.find_all('p')[0].text
#     question = list.find_all('p')[1].text
#     # question2 = list.find_all('p')[2].text

#     info = [text, question]
#     print(info)