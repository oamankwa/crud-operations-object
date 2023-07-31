from flask import Flask
import csv
import datetime
"""
This is a generic crud class. It uses a dictionay to do crud operations

"""

class CreateCrud:

    #ceate variabes
    COLUMNS_ROWS = {}
    DICT_LEN = 0
    A_LIST = [{}] 
    



    #add a constuctor
    def __init__(self, columns_rows, dict_len, new_list):
        self.COLUMNS_ROWS = columns_rows
        self.DICT_LEN = dict_len
        self.A_LIST = new_list
        

    #insert many dictionaries into a table
    def add_many(self, table, mycursor, mydb):
        for self.COLUMNS_ROWS in self.A_LIST:
            rows = ','.join("'"+ str(x).replace('/', '-') + "'" for x in  self.COLUMNS_ROWS.values())
            columns = ','.join(str(x).replace('/', '_') for x in self.COLUMNS_ROWS.keys())
            sql = "INSERT INTO %s (%s)VALUES(%s);" % (table, columns, rows)
            mycursor.execute(sql)
        mydb.commit()

    #insert a dictionary into a table
    def add(self, table, mycursor, mydb):
        columns = ','.join(self.COLUMNS_ROWS.keys())
        rows = ','.join("'"+ str(x).replace('/', '-') + "'" for x in  self.COLUMNS_ROWS.values())
        sql ="INSERT INTO %s ( %s) VALUES (%s)" % (table, columns, rows)
        mycursor.execute(sql)
        mydb.commit()


    #insert values from a csv file into a table
    def add_csv(self, table, file, mlist, mycursor, mydb):
        columns = ','.join(mlist)
        with open(file) as f:
            csvfile = csv.reader(f, delimiter=',')
            for row in csvfile:
                if type(row) == str or type(row) == datetime.date:
                    lines = ','.join("'"+ str(x).replace('/', '-') + "" for x in  row) 
                else:
                    lines = ','.join(""+ str(x).replace('/', '-') + "" for x in  row)
                sql = "INSERT INTO %s (%s) VALUE (%s)" % (table, columns, lines)
                print(sql)
                mycursor.execute(sql)
            mydb.commit()

    # pair two list by elements and they have be the same length
    def pair_list(self, col, rows):
        mylist = []
        for row in rows:
            if type(row) == str or type(row) == datetime.date:
                 mylist = list(map(lambda X:  (X[0]+' = ' + "'" +X[1] + "'"), list(zip(col,rows))))
            else:
                 mylist = list(map(lambda X:  (X[0]+' = ' + str(X[1])), list(zip(col,rows))))
        return mylist

    
    #update fields in a  table. Key and value are used in the where clause
    def update_fields(self, table, col, rows,  key, value, mycursor, mydb):
        mylist = self.pair_list(col, rows)      
        res = ''
        for tup in mylist:
            res += tup + ', '
        # remove the trailing ', '
        res = res[:-2]
        sql = "UPDATE %s SET %s WHERE %s = %s;" %(table, res, key, value)
        mycursor.execute(sql)
        mydb.commit()
 
    
    #retrieve all 
    def get_all(self, table, mycursor):
        mycursor.execute("SELECT * FROM %s;" %(table))
        get_results =  mycursor.fetchall()
        return get_results
  

  
        
    #retrieve a row by key and value
    def get_one(self, table, key, value, mycursor):
        mycursor.execute("SELECT * FROM  %s WHERE %s = %s;" % (table, key, value))
        result = mycursor.fetchone()
        return result
    
    #retrieve a fields by  key and value
    def get_fields(self, table, columns, key, value, mycursor):
        rows = ','.join(str(x).replace('/', '_') for x in columns)
        result = mycursor.execute("SELECT %s FROM  %s WHERE %s = %s;" % (rows, table, key, value))
        result = mycursor.fetchall()
        return result

   
        

    #remove a row from a table by key and value
    def delete(self, table, key, value, mycursor, mydb):
        sql= "DELETE FORM %s WHERE %s = %s;" %(table, key, value)
        print(sql)
        mycursor.execute(sql)
        #mydb.commit()
        
    


    

        
