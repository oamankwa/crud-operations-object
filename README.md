# Generic crud operations objects

This project was intended for useability for crud operations with mysql. 

Normally most crud operations are included in code which makes it difficult to read and understand. This object will make code less difficult to read and will cut down the lines of code. Also it can be inherited and all its methods could be used. Thus, the sub class only has to include specialized methods when needed.

The class of this object is found in the crud.py file. Most crud operations such as create, update, retrieve, and delete can be performed by this object by instantiating the class and adding a dictionary and a list of dictionaries as parameters. Most method parameters are mostly table names and column names.

Also there is a reporting object found in the reports.py file. This class mainly uses the Pandas model for reporting. There is no instantiating of this object, however, it has a method of getting data from any table and storing them in a dataframe. Therefore, using this object many data frames can be created allowing pandas dataframe to perform various operations on them.

**How to Use**

* Import CreateCrud from crud and mysql connector models and instantiate them. Then you can test various methods of the CreateCurd. Before that you also instantiate mysql model  e.g. mydb = mysql.connector.connect(host = ‘your servername’, user= ‘your username’ passwd = ‘your password’, database = ‘your database name’) Then get the cursor e.g mycursor = mydb.cursor(). Add mydb and mycursor as parameters when calling the methods.

* Do not need to instantiate the Reporting object, however, the mysql model has to be instantiated as above. Then, various methods can be implemented as needed. A new release of this object is in the works.

**Features**
* Insert data from a csv file
* Insert multiple rows into a table
* Update multiple columns in a table
* Merge, concatenate, and join various data frames from different tables.

**Links**

* Python documentation:  https://docs.python.org/3/
* Pandas: https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html


