import pandas as pd
import numpy as np
import datetime


class Reporting:
    pass

    # create constuctor
    def __init__(self):
        pass

    # get dataframe from mysql table
    def getdf(self, table, mydb):
        sql = "SELECT * FROM %s;" %(table)
        get_results = pd.read_sql(sql, mydb)
        return get_results.head()

    # combine two dataframes with one column name in both dataframes
    def getmergetwo(self, dframe1, dframe2, col):
        if type(col) == str or type(col) == datetime.date:
            results = pd.merge(dframe1, dframe2, on=str(col))
        else:
            results = pd.merge(dframe1, dframe2, on=col)
        return results.head()

    # combine two dataframes create joins
    def getmergewithhow(self, dframe1, dframe2, khow):
        if type(khow) == str or type(khow) == datetime.date:
            results = pd.merge(dframe1, dframe2, how=str(khow))
        else:
            results = pd.merge(dframe1, dframe2, how=khow)
        return results.head()
    
    # combine two dataframes with indexes
    def getmergetwowithind(self, dframe1, dframe2, inx):
        if type(inx) == str or type(inx) == datetime.date:
            df1 = dframe1.set_index(inx)
            df2 = dframe2.set_index(inx)
            results = pd.merge(df1, df2)
        else:
            df1 = dframe1.set_index(inx)
            df2 = dframe2.set_index(inx)
            results = pd.merge(df1, df2)
        return results.head()
    


    # combine two different dataframes 
    def getmergediffdf(self, dframe1, dframe2, right, left):
        if type(right) == str or type(right) == datetime.date or type(left) == str or type(left) == datetime.date:
            results = pd.merge(dframe1, dframe2, left_on=str(left), right_on=str(right))
        else:
            results = pd.merge(dframe1, dframe2, left_on=left, right_on=right)
        return results.head()


    # combine number a of dataframes
    def getmergedfs(self, dflist):
        result = pd.concat(dflist)
        return result
