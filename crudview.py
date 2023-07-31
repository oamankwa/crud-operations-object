# This file is used to test the crud object
import mysql.connector
from crud import CreateCrud

mydb = mysql.connector.connect(host="Your host", user="Your username", passwd="Your password", database="Your database name")
mycursor = mydb.cursor()


mydict = {'user_id':1,'address':'123 street', 'city': 'Boca Raton', 'state':'Florida'}
mylen = 2
mylist =[{'user_name':'barkokofi','password':'kb1230', 'email': 'kbarko@gmail.com'}, {'user_name':'abenaserwaa','password':'serabe23', 'email': 'aserwaa@gmail.com'}]
mycrud = CreateCrud(mydict, mylen, mylist)

mycolumns = ['user_name', 'email']

mycrud.update_one('users', 'user_name', 'SamDua', 'user_id', 3, mycursor, mydb)
getfields = mycrud.get_fields('users', mycolumns, 'user_id', 2, mycursor)
for i in getfields:
    print(i)
col = ['user_name', 'email']
row = ['Joe Simple', 'jsimple@gmail.com']
mycrud.update_fields('users', col, row, 'user_id', 4, mycursor, mydb )
mycrud.delete('users', 'user_id', 6, mycursor, mydb)
getall = mycrud.get_all('users', mycursor)

for i in getall:
    print(i)

getone = mycrud.get_one('users', 'user_id', 1, mycursor)
print(getone)  
onelist = ['user_id', 'address', 'city', 'state']
mycrud.add_csv('locations','your path/addcsv.csv', onelist, mycursor, mydb)
mycrud.add('users', mycursor, mydb)

mycrud.add_many('users', mycursor, mydb)






