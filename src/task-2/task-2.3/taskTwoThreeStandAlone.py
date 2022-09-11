import pandas as pd
import subprocess
import sys
import psycopg2
#tweak the database parameters to match your specific postgres database.
from pandas.core.frame import DataFrame

def UserInput():
    min_capacity = int(input("What is the clubs with largest number of players in the dataset needed(z) : "))
    return(min_capacity)

def clubs_with_largest_number_of_players():

    min_capacity = UserInput()

    if(isinstance(min_capacity, str)):
        print("Enter the numeric value")
        return(None) 
    else:                
        if(min_capacity < 5):
            print("Please enter the value greater than 5")
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

                query = ("""select club, count(*) as number_of_players from fifa.player_twenty
                group by club
                order by number_of_players desc
                limit  %(min_cap)s """   ) 
                with conn.cursor() as cursor:
                    # Then we pass the param_dict along with the query
                    # string to cursor.execute
                    cursor.execute(query, param_dict)
                    results = cursor.fetchall()
                    clubLargestPlayers = results
                    return(clubLargestPlayers)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print('Database connection closed.')

clubLargestPlayers  = clubs_with_largest_number_of_players()


