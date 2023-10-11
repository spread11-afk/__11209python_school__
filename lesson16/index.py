import dataSource

def main():
    cities = dataSource.cities_info()
    name1 = dataSource.cityNames()
    city = dataSource.info(name='雲林縣土庫鎮')
    #print(name1)
    print(city)
    #print(cities)

if __name__ == "__main__":
    
    main()



#def main():
#    name = dataSource.cityNames()
#    print(name)

#if __name__ == "__main__":
    
#    main()

#def main():
#    cities = dataSource.cities_info()
#    print(cities)

#if __name__ == "__main__":
    
#    main()




#import dataSource

#def main():
#    cities = dataSource.cities_info()
#    for city in cities:
#        print(city)

#if __name__ == "__main__":
#    main()