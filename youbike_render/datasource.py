import requests
import password as pw
import psycopg2

def __download_youbike_data() -> list[dict]:
    '''
    下載台北市youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()


def __create_table(conn)->None:
    cursor = conn.cursor()
    cursor.execute(
        '''
CREATE TABLE  IF NOT EXISTS 台北市youbike(
            "id"	SERIAL,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
            PRIMARY KEY("id"),
            UNIQUE(站點名稱,更新時間) 
        );
        '''
    )
    conn.commit()
    cursor.close()
    print("create_table成功")


def __insert_data(conn, values: list[any]) -> None:
    cursor = conn.cursor()
    sql = '''
    INSERT INTO 台北市youbike(站點名稱,行政區,更新時間,地址,總車輛數,可借,可還)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (站點名稱,更新時間) DO NOTHING
    '''
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()


def updata_sqlite_data() -> None:
    '''
    下載,並更新資料庫
    '''
    data = __download_youbike_data()
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER,
                            password=pw.PASSWORD,
                            host=pw.HOST,
                            port="5432")
    __create_table(conn)
    for item in data:
        __insert_data(conn, [item['sna'], item['sarea'], item['mday'],
                      item['ar'], item['tot'], item['sbi'], item['bemp']])
    conn.close()
