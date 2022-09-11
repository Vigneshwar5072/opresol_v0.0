import pandas as pd
import subprocess
import sys
import psycopg2
#tweak the database parameters to match your specific postgres database.
from pandas.core.frame import DataFrame


def UserInput():
    min_capacity = int(input("How many top most popular nationality for players required? : "))
    return(min_capacity)



def most_popular_nationality(min_capacity):
    #task_two_five = DataFrame()
    #min_capacity = UserInput()
    if(isinstance(min_capacity, str)):
        print("Enter the numeric value")
        return(None) 
    else:                
        if(min_capacity < 0):
            print("Please enter the value greater than 0")
            return(None)
        elif(min_capacity > 200):
            print("Please enter the value lesser than 100")
            return(None)
        else:
            param_dict = { "min_cap": min_capacity }

        
            """ Connect to the PostgreSQL database server """
            conn = None
            try:
                # connect to the PostgreSQL server
                print('Connecting to the PostgreSQL database...')
                conn = psycopg2.connect(host="localhost", 
                                    port="5432", 
                                    user="postgres", 
                                    password="welcome$1234", 
                                    database="postgres")
                cur = conn.cursor()

                query = ("""select nationality, count(*) as popular_nation from fifa.player_twenty
                            group by nationality
                            order by popular_nation desc
                            limit %(min_cap)s """)
                with conn.cursor() as cursor:
                    # Then we pass the param_dict along with the query
                    # string to cursor.execute
                    cursor.execute(query, param_dict)
                    results = cursor.fetchall()
                    popularNation = results
                return(popularNation)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print('Database connection closed.')


#popularNation = most_popular_nationality()
#print(popularNation)


