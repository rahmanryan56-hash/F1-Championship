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



#Function to display a scatter plot
def displayscatter (C1, C2):
    import pandas as mao
    import numpy as nm
    import matplotlib.pyplot as pyp
    pyp.scatter(x= C1, y= C2)
    pyp.show()
    
    

#Function to display a histogram
def displayhistogram (Column_1, Number_Of_Bins):
    import pandas as mao
    import numpy as nm
    import matplotlib.pyplot as pyp
    pyp.hist(Column_1, Number_Of_Bins)
    pyp.show()


    
#Function to display a bar chart 
def displaybar (Val1, Val2):
    import pandas as mao
    import numpy as nm
    import matplotlib.pyplot as pyp
    pyp.bar(Val1, Val2)
    pyp.show()
    
    

    
#Function to display a pie chart
def displaypie (L1, L2):
    import matplotlib.pyplot as pyp
    import numpy as nm
    pyp.pie(L1, labels=L2)
    pyp.show()
