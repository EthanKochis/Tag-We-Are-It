import psycopg2
from data import *

connection = psycopg2.connect(database="project", user ="osc")#, passwrod="", host ="", port="")

cursor = connection.cursor()

for i in range(len(articles)):
    cursor.execute(f"INSERT INTO ARTICLE (Date_published, Author, Title, Body) VALUES ('{articles[i][0]}', '{articles[i][1]}', '{articles[i][2]}', '{articles[i][3]}');")

for i in range(len(tag_categories)):
    cursor.execute(f"INSERT INTO TAG_CATEGORY (Category_name) VALUES ('{tag_categories[i]}');")

for i in range(len(tags)):
    cursor.execute(f"INSERT INTO TAG (Tag_name, Category_name) VALUES ('{tags[i][0]}', '{tags[i][1]}');")

for i in range(len(classified_as)):
    cursor.execute(f"INSERT INTO CLASSIFIED_AS (Article_ID, Tag_name) VALUES({classified_as[i][0]+1}, '{classified_as[i][1]}');")

connection.commit()
cursor.close()
connection.close()


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
