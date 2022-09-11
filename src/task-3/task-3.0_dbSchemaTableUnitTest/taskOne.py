import psycopg2

def create_schema(cur, conn):
    #execute the create statement
        
	# execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)


    cur.execute("CREATE SCHEMA fifa;")
    conn.commit()
    print("schema created successfully")

def create_table(cur, conn):
    #execute the create table statment 
    cur.execute("""CREATE TABLE IF NOT EXISTS fifa.player_twenty(sofifa_id INT NOT NULL PRIMARY KEY,  
                                                            player_url VARCHAR(255) NOT NULL, short_name VARCHAR(255) NOT NULL, long_name VARCHAR(255) NOT NULL,
                                                            age INT, dob DATE, height_cm INT, weight_kg INT, nationality TEXT,
                                                            club VARCHAR(255), overall INT, potential INT, value_eur INT, wage_eur INT,
                                                            player_positions VARCHAR(50), preferred_foot TEXT, international_reputation INT,
                                                            weak_foot INT, skill_moves INT, work_rate VARCHAR(50), body_type VARCHAR(100), 
                                                            real_face BOOLEAN, release_clause_eur INT, player_tags VARCHAR(255),
                                                            team_position VARCHAR(255), team_jersey_number INT, loaned_from VARCHAR(255),
                                                            joined DATE, contract_valid_until VARCHAR(4), nation_position VARCHAR(255), 
                                                            nation_jersey_number INT, pace INT, shooting INT, passing INT, dribbling INT,
                                                            defending INT, physic INT, gk_diving INT, gk_handling INT, gk_kicking INT, 
                                                            gk_reflexes INT, gk_speed INT, gk_positioning INT, player_traits VARCHAR(255),
                                                            attacking_crossing INT, attacking_finishing INT, attacking_heading_accuracy INT, 
                                                            attacking_short_passing INT, attacking_volleys INT, skill_dribbling INT, skill_curve INT,
                                                            skill_fk_accuracy INT, skill_long_passing INT, skill_ball_control INT, 
                                                            movement_acceleration INT, movement_sprint_speed INT, movement_agility INT, 
                                                            movement_reactions INT, movement_balance INT, power_shot_power INT, power_jumping INT, 
                                                            power_stamina INT, power_strength INT, power_long_shots INT, mentality_aggression INT, 
                                                            mentality_interceptions INT, mentality_positioning INT,	mentality_vision INT,
                                                            mentality_penalties INT, mentality_composure INT, defending_marking INT,
                                                            defending_standing_tackle INT, defending_sliding_tackle INT, goalkeeping_diving INT,	
                                                            goalkeeping_handling INT, goalkeeping_kicking INT, goalkeeping_positioning INT,	
                                                            goalkeeping_reflexes INT, ls VARCHAR(25), st VARCHAR(25), rs VARCHAR(25), lw VARCHAR(25),
                                                            lf VARCHAR(25),	cf VARCHAR(25),	rf VARCHAR(25), rw VARCHAR(25), lam VARCHAR(25),
                                                            cam VARCHAR(25), ram VARCHAR(25), lm VARCHAR(25), lcm VARCHAR(25), cm VARCHAR(25), 
                                                            rcm VARCHAR(25), rm VARCHAR(25), lwb VARCHAR(25), ldm VARCHAR(25), cdm VARCHAR(25),	
                                                            rdm VARCHAR(25), rwb VARCHAR(25), lb VARCHAR(25), lcb VARCHAR(25), cb VARCHAR(25), rcb VARCHAR(25),
                                                            rb VARCHAR(25), 
                                                            CONSTRAINT player_url_short_name_long_name  UNIQUE (player_url,short_name, long_name));""")
    
    
    
    conn.commit()
    cur.execute("SELECT * FROM fifa.player_twenty")
    print("player_twenty table created successfully:")
    print (cur.description)
    


def connect():
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
		
        # create a cursor
        cur = conn.cursor()
        # calling the create schema function to create the schema
        create_schema(cur, conn)

        #calling the create table function to create table in the above created schema
        create_table(cur, conn)

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

