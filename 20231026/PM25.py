import requests
import threading
import sqlite3
from password import apikey

# 須先建立password.py存放apikey，才能下載資料
# 即時資料網址:https://data.moenv.gov.tw/swagger/

def download_data() -> dict:
    '''
    下載資料
    '''

    pm25_url = f"https://data.moenv.gov.tw/api/v2/aqx_p_02?language=zh&api_key={apikey}"
    response = requests.get(pm25_url)
    response.raise_for_status()
    print('下載成功')
    data = response.json()



