from os import read
import pandas as pd
import subprocess
import sys
import psycopg2
#tweak the database parameters to match your specific postgres database.
from pandas.core.frame import DataFrame

def UserInput():
    min_capacity = int(input("Enter the required top performers list : "))
    return(min_capacity)
    


def skillset(min_capacity):

    skillSet = ['attacking_crossing',	'attacking_finishing',	'attacking_heading_accuracy',	
                'attacking_short_passing',	'attacking_volleys',	'skill_dribbling',
                'skill_curve',	'skill_fk_accuracy',	'skill_long_passing',	'skill_ball_control',
                'movement_acceleration',	'movement_sprint_speed',	'movement_agility',
                'movement_reactions',	'movement_balance',	'power_shot_power',	'power_jumping',
                'power_stamina',	'power_strength',	'power_long_shots',	'mentality_aggression',
                'mentality_interceptions',	'mentality_positioning',	'mentality_vision',	
                'mentality_penalties',	'mentality_composure',	'defending_marking',	
                'defending_standing_tackle',	'defending_sliding_tackle',	
                'goalkeeping_diving',	'goalkeeping_handling',	'goalkeeping_kicking',
                'goalkeeping_positioning',	'goalkeeping_reflexes']

    #min_capacity = UserInput()

    if(isinstance(min_capacity, str)):
        print("Enter the numeric value")
        return(None, None) 
    else:                
        if(min_capacity < 0):
            print("Please enter the value greater than zero")
            return(None, None)
        elif(min_capacity > 100):
            print("Please enter the value lesser than 100")
            return(None, None)
        else:
            param_dict = { "min_cap": min_capacity }
            return(skillSet, param_dict)


def top_improvements(min_capacity):
    [skillSet,param_dict] = skillset(min_capacity)
    improvement = {}
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


        for i in skillSet:
            print(i)
            query = ("""select  sofifa_id, 
                                (((select avg(""" + i + """) 
                                from fifa.player_twenty)-""" + i + """)/(select avg(""" + i + """) 
                                from fifa.player_twenty)*100) as improvement
                                from fifa.player_twenty
                                order by improvement desc 
                                limit %(min_cap)s """   ) 

            with conn.cursor() as cursor:
                # Then we pass the param_dict along with the query
                # string to cursor.execute
                cursor.execute(query, param_dict)

                results = cursor.fetchall()

                improvement[i] = results
        return(improvement)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

top_performed_improvement  = top_improvements()
