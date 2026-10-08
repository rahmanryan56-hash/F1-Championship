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



#Function readcsv is used to read csv files from a particular location, once the function reads the csv files it saves as a dataframe and returns as a dataframe
def readcsv(loca, filename):
    import pandas as mao
    loc=loca 
    fname=filename
    locate_file=loc+fname
    print(locate_file)
    df=mao.read_csv(locate_file)
    return df


#Function is used to write csv files into the database
#To write it, the df and table_name need to be passed
#Write df1.to_sql to create the table and write return table_name to return the table. The table is created inside the database
def writecsv_to_db(DataFrame, table_name):
    import pandas as mao
    df1=DataFrame
    table=table_name
    print(table)
    df1.to_sql(table, connection, if_exists='replace', index=False)
    return table_name
