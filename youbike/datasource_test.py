import requests
import sqlite3


def __download_youbike_data()->list[dict]:
    '''
    下載youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()

def __create_table(con):
	cursor = con.cursor()
	cursor.execute(
		'''
		CREATE TABLE   IF NOT EXISTS 台北市youbike(
			"id"	INTEGER,
			"站點名稱"	TEXT NOT NULL,
			"行政區"	TEXT NOT NULL,
			"更新時間"	TEXT NOT NULL,
			"地址"	TEXT,
			"總車輛數"	INTEGER,
			"可借"	INTEGER,
			"可還"	INTEGER,
			'測試'	INTEGER,
			PRIMARY KEY("id" AUTOINCREMENT)
		);

		'''
	)
	con.commit()

def update_data_to_sqlite():
    '''下載、更新資料'''
    data = __download_youbike_data()
    conn = sqlite3.connect('youbike.db')
    __create_table(conn)
    
    
