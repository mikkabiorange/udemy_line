#!/usr/bin/env python
# coding: utf-8

# In[ ]:


token="4z5ABFP4UWBFxEoLaU3ZvT4V5fkVLxx5vuSGUsvZKSM"
url="https://notify-api.line.me/api/notify"


# In[ ]:


import requests



# In[ ]:


auth={"Authorization":"Bearer "+token}
content={"message":'123'}


# In[ ]:


requests.post(url, headers=auth, data=content)

# %%

# %%

# %%

# %%

# %%
