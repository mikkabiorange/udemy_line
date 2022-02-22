#!/usr/bin/env python
# coding: utf-8

# In[ ]:


token="4z5ABFP4UWBFxEoLaU3ZvT4V5fkVLxx5vuSGUsvZKSM"
url="https://notify-api.line.me/api/notify"


# In[ ]:


import requests



# In[ ]:


tenki_url="https://weather.yahoo.co.jp/weather/jp/22/5040.html"


# In[ ]:


Response=requests.get(tenki_url)


# In[ ]:


Response.text





# In[ ]:


requests.post(url, headers=auth, data=content)

# %%

# %%

# %%

# %%

# %%
