#!/usr/bin/env python
# coding: utf-8

# In[ ]:


token="4z5ABFP4UWBFxEoLaU3ZvT4V5fkVLxx5vuSGUsvZKSM"
url="https://notify-api.line.me/api/notify"


# In[ ]:

import requests


# In[ ]:

import datetime
dt = datetime.date.today()
tstr = tdatetime.strftime('%Y/%m/%d')
auth={"Authorization":"Bearer "+token}
content={"message":'坂本様の手下のpythonです。よろしくお願いします。一時間に一度実行されます。只今の時刻、'+tstr}


# In[ ]:


requests.post(url, headers=auth, data=content)

# %%

# %%

# %%

# %%

# %%
