import pytest
from taskOne import *


def test_happypath_dbConnection():
    conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="welcome$1234", 
                        database="postgres")
		
        # create a cursor
    cur = conn.cursor()
    test_schema = create_schema(cur, conn)
    test_table = create_table(cur, conn)
    
def test_sadPath():
    #connected to wrong database and check for the expected outcome
    connect()


if __name__ == "__main__":
    test_happypath_dbConnection()
    test_sadPath()
    print("Everything passed")
