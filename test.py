DATABASES = ["pay","payments"]
CDC_DATABASES =  [["pay","payments"]]


for database in DATABASES:
    print(database)

for database in CDC_DATABASES:
    for x in range(len(database)):
        print(database[x])


        #teste2 