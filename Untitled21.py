#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests as re
data  = re.get('https://www.worldometers.info/coronavirus/')
news_html = re.get('https://www.google.com/search?q=corona+news+india+english&ie=UTF-8&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjg1Mn_upLoAhXZgUsFHfsPAtMQ_AUICygE')


# In[20]:


from bs4 import BeautifulSoup
data = data.content
soup = BeautifulSoup(data, "html")
table = soup.find("table")


# In[21]:


total = []
#soup = table.select('tr:has(> td:contains("India"))')
for tr in soup.findAll("table"):
    for td in tr.find_all("td"):
        if not td.attrs.get('style'):
            total.append (td.text)
total


# In[22]:


all_ = []
#soup = table.select('tr:has(> td:contains("India"))')
for tr in soup.findAll("table"):
    for td in tr.find_all("td"):
        if td.attrs.get('style'):
            all_.append (td.text)


# In[23]:


data_of_india = []
index_of_india = (all_.index(' India '))
for i in range(index_of_india,index_of_india+9):
    data_of_india.append(all_[i])


# In[24]:


data_of_india1 = []
for every in data_of_india:
    if every == ' ':
        every = 0
        data_of_india1.append(every)
    else:
        data_of_india1.append(every)


# In[25]:


soup = BeautifulSoup(news_html.content, 'lxml')
news_links = []
for link in soup.find_all('a'):
    news_links.append(link.get('href'))

comp_link = []
for every in news_links:
    every = 'https://www.google.com'+every
    comp_link.append(every)


# In[28]:


print(f'''Hello Team,

Good Evening!

Today's Corona stats in World:

Total Cases : {total[1]}
Total Death : {total[2]}
Total Recovered :{total[3]}
Active Cases :{total[4]}
Serious:{total[5]}


Today's Corona stats in India:

Total Cases : {data_of_india1[1]}
Total Death : {data_of_india1[3]}
Total Recovered :{data_of_india1[5]}
Active Cases :{data_of_india1[6]}
Serious : {data_of_india1[7]}

Today's Top News:
{comp_link[21]}
{comp_link[23]}
{comp_link[25]}


''')


# In[ ]:


import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = '    '
mail.Subject = 'Corona Stats and Top News'
mail.Body = f'''Hello Team,

Good Evening!

Today's Corona stats in World:

Total Cases : {total[1]}
Total Death : {total[2]}
Total Recovered :{total[3]}
Active Cases :{total[4]}
Serious:{total[5]}


Today's Corona stats in India:

Total Cases : {data_of_india1[1]}
Total Death : {data_of_india1[3]}
Total Recovered :{data_of_india1[5]}
Active Cases :{data_of_india1[6]}
Serious : {data_of_india1[7]}

Today's Top News:
{comp_link[21]}
{comp_link[23]}
{comp_link[25]}


'''


mail.Send()
'''attachment  = "Path to the attachment"
mail.Attachments.Add(attachment)'''


# In[ ]:




