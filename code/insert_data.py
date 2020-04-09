import psycopg2
from data import *
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % params['database'])
        conn = psycopg2.connect(**params)
        print('Connected.\n')

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version[0])

        # Insert articles
        for i in range(len(articles)):
            cur.execute(f"INSERT INTO ARTICLE (Date_published, Author, Title, Body) VALUES ('{articles[i][0]}', '{articles[i][1]}', '{articles[i][2]}', '{articles[i][3]}');")

        # Insert tag_categories
        for i in range(len(tag_categories)):
            cur.execute(f"INSERT INTO TAG_CATEGORY (Category_name) VALUES ('{tag_categories[i]}');")

        # Insert tags
        for i in range(len(tags)):
            cur.execute(f"INSERT INTO TAG (Tag_name, Category_name) VALUES ('{tags[i][0]}', '{tags[i][1]}');")

        # Insert classified_as
        for i in range(len(classified_as)):
            cur.execute(f"INSERT INTO CLASSIFIED_AS (Article_ID, Tag_name) VALUES({classified_as[i][0]+1}, '{classified_as[i][1]}');")

        conn.commit()

        print("Insertions completed successfully!")
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('\nDatabase connection closed.')

if __name__ == '__main__':
    connect()

'''
# Insert into ARTICLE
INSERT INTO ARTICLE (Date_published, Author, Title, Body)
VALUES ('2017-03-19', 'Georgina Smith', 'Organization does Good Thing', 'Yesterday morning an organization...');

# Insert into TAG
INSERT INTO TAG (Name, Category_name)
	VALUES ("beach cleanup", "climate action");

# Insert into TAG_CATEGORY
INSERT INTO TAG_CATEGORY (Name)
	VALUES ("climate action");

# Insert into CLASSIFIED_AS
INSERT INTO CLASSIFIED_AS (Article_ID, Tag_name)
	VALUES(1, 'beach cleanup');
'''
