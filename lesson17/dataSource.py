import requests,csv,io

__ceties = []

def __download()->list[list]:
    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=apikey'

    response = requests.request('GET',url)
    try:
        response.raise_for_status()
    except:
        raise Exception("連線錯誤","網路中斷")
        
    else:    
        if not response.ok:
            raise Exception("下載失敗","伺服器錯誤")
            
        else:
            file = io.StringIO(response.text)
            csv_reader = csv.reader(file)
            next(csv_reader)
            return list(csv_reader)
        
            
def cities_info()->list[list]:
    if len(__ceties)==0:
        try:
            data_list = __download()
        except Exception as e:
            print(f"錯誤:{e}")
        else:
            for row in data_list:  
                if row[0] == "111":
                    __ceties.append(row)
    return __ceties    



def cityNames() -> list[list]:
    cities = cities_info()
    name1 = []
    for row in cities:
        
        name1.append(row[1])
    return name1

def info(name:str):
    cities = cities_info()
    for row in cities:
        if row[1]==name:
            return row
        
    return[]    




#def cities_info() -> list[list]:
#    cities = []
#    try:
#        data_list = __download()    
#    except Exception as e:
#        print(f"錯誤:{e}")
#    else:
#        for row in data_list:
#            if row[0] == '111':
#                cities.append(row)
#    return cities