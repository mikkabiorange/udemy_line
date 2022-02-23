#!/usr/bin/env python
# coding: utf-8

# In[ ]:


token="4z5ABFP4UWBFxEoLaU3ZvT4V5fkVLxx5vuSGUsvZKSM"
url="https://notify-api.line.me/api/notify"


import requests


# In[ ]:

from datetime import datetime, timedelta, timezone
# 日本時間のタイムゾーンを定義
JST = timezone(timedelta(hours=+9), 'JST')
# Pythonが動くサーバーのタイムゾーン設定に左右されずに日本時間の現在時刻を取得
dt = datetime.now(JST)
# ISO8601形式で表示
dt.isoformat() # -> 2021-04-14T01:57:42.809986+09:00
tstr = dt.strftime('%Y/%m/%d')
content={"message":'Pythonです。本日の日付は、'+tstr}
auth={"Authorization":"Bearer "+token}

# In[ ]:


requests.post(url, headers=auth, data=content)

# %%

# %%

# %%

# %%

# %%
