import pandas as pd
import subprocess
import sys
import psycopg2
#tweak the database parameters to match your specific postgres database.
from pandas.core.frame import DataFrame


def UserInput():
    min_capacity = int(input("What is the number of top popular nation and team position required? : "))
    return(min_capacity)

def most_popular_nation_and_team_position():

    min_capacity = UserInput()
    if(isinstance(min_capacity, str)):
        print("Enter the numeric value")
        return(None) 
    else:                
        if(min_capacity < 0):
            print("Please enter the value greater than 0")
            return(None)
        elif(min_capacity > 100):
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



                query1 = ( """ select nation_position, count(*) as popular_nation from fifa.player_twenty
                            group by nation_position
                            order by popular_nation desc
                            offset 1 limit %(min_cap)s """   ) 
                with conn.cursor() as cursor:
                    # Then we pass the param_dict along with the query
                    # string to cursor.execute
                    cursor.execute(query1, param_dict)
                    results1 = cursor.fetchall()
                    nationPosition = results1

                query2 = (""" select team_position, count(*) as popular_team from fifa.player_twenty
                            group by team_position
                            order by popular_team desc
                            limit  %(min_cap)s """   ) 
                with conn.cursor() as cursor:
                    # Then we pass the param_dict along with the query
                    # string to cursor.execute
                    cursor.execute(query2, param_dict)
                    results2 = cursor.fetchall()
                    teamPositon = results2        
                    return(nationPosition, teamPositon)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print('Database connection closed.')

[nationPosition, teamPositon]  = most_popular_nation_and_team_position()
print([nationPosition, teamPositon])

