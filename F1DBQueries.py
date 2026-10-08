#Function creates an SQLite3 database 
def create_Sqlite_connection(location_path, database_name):
    import sqlite3 as sql
    global connection
    connection=None
    location=location_path
    F1ResultsDB=database_name
    conn=location+F1ResultsDB
    
    
    #checking location of the database
    print(conn)
    
    
    #creating new database
    connection=sql.connect(conn)
    print('The Database has been Created.')
    connection.commit()
    print('Changes have been Saved.')
    return connection 

    
    
#returning results of the query execution as a dataframe
def displaydbtable(query_string, DataFrame):
    import pandas as mao
    query_str=query_string
    print(query_str)
    df= DataFrame
    print(DataFrame)
    
