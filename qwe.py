#!/usr/bin/env python
# coding: utf-8

# In[ ]:


token="4z5ABFP4UWBFxEoLaU3ZvT4V5fkVLxx5vuSGUsvZKSM"
url="https://notify-api.line.me/api/notify"


# In[ ]:


from bs4 import BeautifulSoup


# In[ ]:


tenki_url="https://weather.yahoo.co.jp/weather/jp/22/5040.html"


# In[ ]:


Response=requests.get(tenki_url)


# In[ ]:


Response.text


# In[ ]:


html=BeautifulSoup(Response.text,"html.parser")


# In[ ]:


forecast=html.find_all("div",attrs={"class":"forecastCity"})[0]


# In[ ]:


tomorrow=forecast.find_all("div")[1]


# In[ ]:


weather=tomorrow.find_all("p",attrs={"class":"pict"})[0].text.replace("\n","").replace(" ","")


# In[ ]:


high=tomorrow.find_all("li")[0].text


# In[ ]:


low=tomorrow.find_all("li")[1].text


# In[ ]:


rain_06=tomorrow.find_all("td")[4].text
rain_612=tomorrow.find_all("td")[5].text
rain_1218=tomorrow.find_all("td")[6].text
rain_1824=tomorrow.find_all("td")[7].text


# In[ ]:


message="""
明日の天気は{}
a最高気温は{}
最低気温は{}
0-6時:{}
6-12時:{}
12-18時:{}
18-24時:{}
""".format(weather,high,low,rain_06,rain_612,rain_1218,rain_1824)

# In[ ]:


auth={"Authorization":"Bearer "+token}
content={"message":message}


# In[ ]:


requests.post(url, headers=auth, data=content)

# %%

