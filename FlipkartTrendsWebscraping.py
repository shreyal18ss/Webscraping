#Webscraping Flipkart and finding trends on Iphones

#!/usr/bin/env python
# coding: utf-8

# In[195]:


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import re


# In[84]:


my_url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
client=req(my_url)
page=client.read()
client.close()


# In[85]:


soup_page=soup(page,"html.parser")
containers=soup_page.findAll("div",{"class":"_1UoZlX"})


# In[86]:


print(len(containers))


# In[87]:


print(soup.prettify(containers[0]))


# In[88]:


container=containers[0]
print(container.div.img["alt"])


# In[89]:


price=container.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
print(price[0].text)


# In[90]:


rating=container.find_all("div",{"class":"hGSR34"})
print(rating[0].text)


# In[91]:


filename="iphones.csv"


# In[92]:


f=open(filename,"w")
header="Product_Name,Pricing,Rating\n"
f.write(header)


# In[93]:


for container in containers:
    name=container.div.img["alt"]
    priceF=container.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
    price=priceF[0].text.strip()
    ratingF=container.find_all("div",{"class":"hGSR34"})
    rating=ratingF[0].text.strip()
    price=re.sub(r'[^\w]', '', price)
    s=name+" ,"+price+","+rating+'\n'

    print(s)
    f.write(s)


# In[94]:


f.close()


# In[176]:


import pandas as pd
csvFile=pd.read_csv(filename)


# In[184]:


print(csvFile['Rating'])
x=pd.Series(csvFile['Rating'])


# In[190]:


print(csvFile['Pricing'])
z=pd.Series(csvFile['Pricing'])
print(z)


# In[182]:


from matplotlib import pyplot as plt


# In[192]:


Liking=pd.DataFrame({"Rate":x,"Price":z})
print(Liking)


# In[193]:


plt.plot(x,z)
plt.scatter(x,z)


# In[194]:


Liking.describe()


# In[ ]:




